class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        front=[0]*n
        for j in range(n):
            front[j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            cur=[0]*(i+1)
            for j in range(i,-1,-1):
                down=triangle[i][j]+front[j]
                diagonal=triangle[i][j]+front[j+1]
                cur[j]=min(down,diagonal)
            front=cur
        return front[0]