class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt=0
        s=s.lower()
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                cnt+=1
        return cnt