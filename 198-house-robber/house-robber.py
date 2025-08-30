class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=prev2
            nonPick=0+prev
            cur_i=max(pick,nonPick)
            prev2=prev
            prev=cur_i
        return prev