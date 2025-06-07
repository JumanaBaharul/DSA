class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        def lowerbound(nums,target):
            low,high=0,n-1
            ans=n
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        start=lowerbound(nums,target)
        end=lowerbound(nums,target+1)-1
        if start>=n or nums[start]!=target:
            return [-1,-1]
        return [start,end]
