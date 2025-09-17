class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        front=[[0]*n for _ in range(n)]
        cur=[[0]*n for _ in range(n)]

        for j1 in range(n):
            for j2 in range(n):
                if j1==j2:
                    front[j1][j2]=grid[m-1][j1]
                else:
                    front[j1][j2]=grid[m-1][j1]+grid[m-1][j2]

        for i in range(m-2,-1,-1):
            for j1 in range(n):
                for j2 in range(n):
                    maxi=-sys.maxsize

                    for di in range(-1,2):
                        for dj in range(-1,2):
                            ans=0
                            if j1==j2:
                                ans=grid[i][j1]
                            else:
                                ans=grid[i][j1]+grid[i][j2]
                            if ((j1+di<0 or j1+di>=n) or (j2+dj<0 or j2+dj>=n)):
                                ans+=float('-inf')
                            else:
                                ans+=front[j1+di][j2+dj]
                            maxi=max(ans,maxi)
                    cur[j1][j2]=maxi
            front=[row[:] for row in cur]
        return front[0][n-1]