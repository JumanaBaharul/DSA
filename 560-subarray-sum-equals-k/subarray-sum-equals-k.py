from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        mpp=defaultdict(int)
        prefixsum=0
        cnt=0
        mpp[0]=1
        for i in range(n):
            prefixsum+=nums[i]
            remove=prefixsum-k
            cnt+=mpp[remove]
            mpp[prefixsum]+=1
        return cnt