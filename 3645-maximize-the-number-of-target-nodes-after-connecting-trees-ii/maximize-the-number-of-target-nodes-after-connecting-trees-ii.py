class Solution(object):
    def maxTargetNodes(self, edges1, edges2):
        def buildList(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def dfsColor(adj, u, parent, color, counts):
            if color[u] == 0:
                counts["even"] += 1
            else:
                counts["odd"] += 1
            for v in adj[u]:
                if v != parent:
                    color[v] = color[u] ^ 1
                    dfsColor(adj, v, u, color, counts)

        adjA = buildList(edges1)
        adjB = buildList(edges2)

        n, m = len(adjA), len(adjB)
        colorA = [-1] * n
        colorB = [-1] * m

        colorA[0] = 0
        countsA = {"even": 0, "odd": 0}
        dfsColor(adjA, 0, -1, colorA, countsA)

        colorB[0] = 0
        countsB = {"even": 0, "odd": 0}
        dfsColor(adjB, 0, -1, colorB, countsB)

        maxB = max(countsB["even"], countsB["odd"])

        res = []
        for i in range(n):
            if colorA[i] == 0:
                res.append(countsA["even"] + maxB)
            else:
                res.append(countsA["odd"] + maxB)
        return res
