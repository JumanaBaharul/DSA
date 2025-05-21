class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n,m=len(matrix), len(matrix[0])
        zero_cells=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    zero_cells.add((i,j))
        for row,col in zero_cells:
            for i in range(n):
                matrix[i][col]=0
            for j in range(m):
                matrix[row][j]=0           