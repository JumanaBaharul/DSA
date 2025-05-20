class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        temp=[0]*(n+1)
        for l,r in queries:
            temp[l]+=1
            temp[r+1]-=1
        cur = 0
        for i in range(n):
            cur+=temp[i]
            if cur<nums[i]:
                return False
        return True