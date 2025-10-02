class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor:
            return 1
        sign=True
        if (dividend>=0 and divisor<0) or (dividend<=0 and divisor>0):
            sign=False
        n=abs(dividend)
        d=abs(divisor)
        quotient=0
        while n>=d:
            cnt=0
            while n>=(d<<(cnt+1)):
                cnt+=1
            quotient+=(1<<cnt)
            n-=(d<<cnt)
        if quotient==(1<<31) and sign:
            return (1<<31)-1
        if quotient==(1<<31) and not sign:
            return -(1<<31)
        return quotient if sign else -quotient