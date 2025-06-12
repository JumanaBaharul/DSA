class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        maxi=abs(nums[n-1]-nums[0])
        for i in range(n):
            diff=abs(nums[i]-nums[i-1])
            maxi=max(maxi,diff)
        return maxi