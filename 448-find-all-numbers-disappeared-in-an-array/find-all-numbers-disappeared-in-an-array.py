class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for i in range(1, len(nums) + 1):
            if count[i]==0:
                res.append(i)
        return res