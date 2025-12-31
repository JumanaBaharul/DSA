class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        iniColor=image[sr][sc]
        ans=image
        deltaRow=[-1,0,+1,0]
        deltaCol=[0,-1,0,+1]
        self.dfs(sr,sc,ans,image,color,deltaRow,deltaCol,iniColor)
        return ans

    def dfs(self,row,col,ans,image,color,deltaRow,deltaCol,iniColor):
        ans[row][col]=color
        m=len(image)
        n=len(image[0])
        for i in range(4):
            nrow=row+deltaRow[i]
            ncol=col+deltaCol[i]
            if (nrow>=0 and nrow<m and ncol>=0 and ncol<n and image[nrow][ncol]==iniColor and ans[nrow][ncol]!=color):
                self.dfs(nrow,ncol,ans,image,color,deltaRow,deltaCol,iniColor)