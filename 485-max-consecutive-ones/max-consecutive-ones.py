class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        cnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
                maxi=max(maxi,cnt)
            else:
                cnt=0
        return maxi
