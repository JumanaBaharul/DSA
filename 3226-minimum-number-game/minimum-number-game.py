class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        nums.reverse()
        while len(nums)>0:
            mini1=nums[-1]
            nums.pop()
            mini2=nums[-1]
            nums.pop()
            arr.append(mini2)
            arr.append(mini1)
        return arr