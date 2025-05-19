class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = nums
        # Check if it's a valid triangle
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        
        # Triangle is valid, now classify
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"