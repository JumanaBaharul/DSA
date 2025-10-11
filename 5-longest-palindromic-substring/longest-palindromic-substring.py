class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        start,end=0,0
        
        for center in range(len(s)):
            len1=self.expandFromCenter(s,center,center)
            len2=self.expandFromCenter(s,center,center+1)
            maxi=max(len1,len2)
            if maxi>end-start:
                start=center-(maxi-1)//2
                end=center+maxi//2
        return s[start:end+1]

    def expandFromCenter(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    