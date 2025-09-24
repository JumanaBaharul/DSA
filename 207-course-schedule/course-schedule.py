class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        q=deque([i for i in range(numCourses) if indegree[i]==0])
        cnt=0
        while q:
            course=q.popleft()
            cnt+=1
            for neighbor in adj[course]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        return sum(indegree)==0