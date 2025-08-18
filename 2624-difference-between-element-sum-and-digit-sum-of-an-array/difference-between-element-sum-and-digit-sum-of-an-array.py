class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum=sum(nums)
        digit_sum=0
        for num in nums:
            if num<10:
                digit_sum+=num
            else:
                n=num
                while n>0:
                    digit=n%10
                    digit_sum+=digit
                    n=n//10
        return abs(ele_sum-digit_sum)