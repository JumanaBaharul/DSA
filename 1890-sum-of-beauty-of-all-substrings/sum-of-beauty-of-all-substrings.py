class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        total=0
        for i in range(n):
            dic=defaultdict(int)
            mini=0
            maxi=0
            for j in range(i,n):
                dic[s[j]]+=1
                if dic[s[j]]==maxi+1:
                    maxi=dic[s[j]]
                if mini==0 or dic[s[j]]<=mini+1:
                    mini=min(dic.values())
                total+=maxi-mini
        return total