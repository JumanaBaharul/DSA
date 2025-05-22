class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        majorityele=None
        for i in nums:
            if c==0:
                majorityele=i
                c=1
            elif majorityele==i:
                c+=1
            else:
                c-=1
        return majorityele