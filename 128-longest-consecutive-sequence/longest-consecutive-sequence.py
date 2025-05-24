class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        longest=1
        st=set()
        for i in range(n):
            st.add(nums[i])
        for j in st:
            if j-1 not in st:
                x=j
                cnt=1
                while x+1 in st:
                    cnt+=1
                    x+=1
                longest=max(longest,cnt)
        return longest