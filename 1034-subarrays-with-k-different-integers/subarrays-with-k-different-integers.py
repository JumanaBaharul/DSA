class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostk(nums,k)-self.atMostk(nums,k-1)

    def atMostk(self,nums,k):
        freq={}
        left=0
        cnt=0
        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]]==0:
                k-=1
            freq[nums[right]]=freq.get(nums[right],0)+1
            while k<0:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    k+=1
                left+=1
            cnt+=(right-left+1)
        return cnt