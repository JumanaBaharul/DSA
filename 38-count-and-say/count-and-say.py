class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        def say(s):
            s=str(s)
            result=[]
            cnt=1
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    cnt+=1
                else:
                    result.append(str(cnt)+s[i-1])
                    cnt=1
            result.append(str(cnt)+s[-1])
            return ''.join(result)

        current=1
        for _ in range(n-1):
            current=say(current)
        return current