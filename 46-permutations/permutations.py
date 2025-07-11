class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def permutations(ind:int):
            if ind==len(nums):
                ans.append(nums[:])
                return 
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                permutations(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
        permutations(0)
        return ans