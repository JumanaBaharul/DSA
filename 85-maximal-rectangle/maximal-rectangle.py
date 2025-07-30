class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        maxArea=0
        prefixSum=[[0]*m for _ in range(n)]
        for j in range(m):
            total=0
            for i in range(n):
                if int(matrix[i][j])==1:
                    total+=1
                else:
                    total=0
                prefixSum[i][j]=total
            for i in range(n):
                maxArea=max(maxArea,self.lHist(prefixSum[i]))
        return maxArea
    
    def lHist(self,heights:List[int])->int:
        maxArea=0
        st=[]
        for i in range(len(heights)+1):
            h=heights[i] if i<len(heights) else 0
            while st and heights[st[-1]]>h:
                height=heights[st.pop()]
                width=i if not st else i-st[-1]-1
                maxArea=max(maxArea,height*width)
            st.append(i)
        return maxArea