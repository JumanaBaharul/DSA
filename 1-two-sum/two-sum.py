class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    return [i,j]