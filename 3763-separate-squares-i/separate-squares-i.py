class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        minY=0.0
        maxY=0.0
        total=0.0

        for x,y,l in squares:
            if y+l>maxY:
                maxY=y+l
            total+=l*l

        while maxY-minY>10**-5:
            mid=(minY+maxY)/2
            below=0.0

            for x,y,l in squares:
                if y<mid:
                    below+=l*min(l,mid-y)

            if below<total/2:
                minY=mid
            else:
                maxY=mid

        return minY