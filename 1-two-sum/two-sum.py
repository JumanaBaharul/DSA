class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        for index,value in enumerate(nums):
            required=target-value
            if required in hash_map:
                return [hash_map[required],index]
            hash_map[value]=index