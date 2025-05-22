class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        n=len(nums)
        maxi=-sys.maxsize-1
        s=0
        for i in range(n):
            s+=nums[i]
            if s>maxi:
                maxi=s
            if s<0:
                s=0
        return maxi