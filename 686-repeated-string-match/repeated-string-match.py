class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c=a
        cnt=1
        while len(c)<len(b)+len(a):
            if b in c:
                return cnt
            c+=a
            cnt+=1
        if b in c:
            return cnt
        return -1