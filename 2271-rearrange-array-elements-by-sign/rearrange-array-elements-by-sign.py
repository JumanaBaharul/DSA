class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n=len(nums)
        # ans=[0]*n
        # posindex=0
        # negindex=1
        # for i in range(n):
        #     if nums[i]<0:
        #         ans[negindex]=nums[i]
        #         negindex+=2
        #     else:
        #         ans[posindex]=nums[i]
        #         posindex+=2
        # return ans
        ansarray=[0]*len(nums)
        pos,neg=0,1
        for i in range(len(nums)):
            if nums[i]>0:
                ansarray[pos]=nums[i]
                pos+=2
            else:
                ansarray[neg]=nums[i]
                neg+=2
        return ansarray