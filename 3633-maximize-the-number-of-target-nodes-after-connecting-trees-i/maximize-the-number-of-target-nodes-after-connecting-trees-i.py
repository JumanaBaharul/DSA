class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def to_graph(edges):
            graph = [[] for _ in range(len(edges) + 1)]
            for from_node, to_node in edges:
                graph[from_node].append(to_node)
                graph[to_node].append(from_node)
            return graph
        
        def number_of_target_nodes_from(graph, start, k):
            if k < 0:
                return 0
            visited = [False] * len(graph)
            queue = deque([(start, 0)])
            visited[start] = True
            count = 0
            while queue:
                count += 1
                from_node, distance = queue.popleft()
                for to_node in graph[from_node]:
                    if not visited[to_node] and distance < k:
                        visited[to_node] = True
                        queue.append((to_node, distance + 1))
            return count
        
        graph2 = to_graph(edges2)
        max2 = max(number_of_target_nodes_from(graph2, i, k - 1) for i in range(len(graph2)))
        
        graph1 = to_graph(edges1)
        return [number_of_target_nodes_from(graph1, i, k) + max2 for i in range(len(graph1))]