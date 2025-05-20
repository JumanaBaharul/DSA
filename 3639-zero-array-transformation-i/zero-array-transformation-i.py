class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        count = [0] * n
        count[0] = diff[0]
        for i in range(1, n):
            count[i] = count[i - 1] + diff[i]

        for i in range(n):
            if count[i] < nums[i]:
                return False
        return True