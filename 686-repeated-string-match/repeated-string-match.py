class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        cnt=1
        repeated=a
        while len(repeated)<len(b):
            repeated=repeated+a
            cnt+=1
        if b in repeated:
            return cnt
        repeated=repeated+a
        cnt+=1
        if b in repeated:
            return cnt
        return -1