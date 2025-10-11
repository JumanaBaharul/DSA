class Solution:
    def countAndSay(self, n: int) -> str:
        res="1"
        for i in range(1,n):
            curr=""
            cnt=1
            for j in range(1,len(res)):
                if res[j]==res[j-1]:
                    cnt+=1
                else:
                    curr+=str(cnt)+res[j-1]
                    cnt=1
            curr+=str(cnt)+res[-1]
            res=curr
        return res