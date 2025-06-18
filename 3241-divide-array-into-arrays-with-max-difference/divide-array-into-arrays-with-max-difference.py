class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        a=[]
        n=len(nums)
        nums.sort()
        for i in range(0,n-2,3): 
            if nums[i+2]-nums[i]>k:
                return [] 
            a.append(nums[i:i+3])
        return a