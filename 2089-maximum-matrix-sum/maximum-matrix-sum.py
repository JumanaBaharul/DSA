class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_sum=0
        min_abs=float('inf')
        negative_cnt=0

        for row in matrix:
            for val in row:
                abs_sum+=abs(val)
                min_abs=min(min_abs,abs(val))
                if val<0:
                    negative_cnt+=1
        if negative_cnt%2==1:
            abs_sum-=2*min_abs
        return abs_sum