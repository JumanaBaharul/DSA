class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[0]*n
        posindex=0
        negindex=1
        for i in range(n):
            if nums[i]<0:
                ans[negindex]=nums[i]
                negindex+=2
            else:
                ans[posindex]=nums[i]
                posindex+=2
        return ans