class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        rev=s[::-1]
        combined=s+'#'+rev
        sp=[0]*len(combined)

        for i in range(1,len(combined)):
            j=sp[i-1]
            while j>0 and combined[i]!=combined[j]:
                j=sp[j-1]
            if combined[i]==combined[j]:
                j+=1
            sp[i]=j
        return rev[:len(s)-sp[-1]]+s