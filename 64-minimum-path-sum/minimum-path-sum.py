class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for j in range(n)] for i in range(m)]
        return self.miniPathSum(m-1,n-1,grid,dp)
    def miniPathSum(self,i:int,j:int,grid: List[List[int]],dp) -> int:   
        if i==0 and j==0:
            return grid[0][0]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        up=grid[i][j]+self.miniPathSum(i-1,j,grid,dp)
        left=grid[i][j]+self.miniPathSum(i,j-1,grid,dp)
        dp[i][j]=min(up,left)
        return dp[i][j]