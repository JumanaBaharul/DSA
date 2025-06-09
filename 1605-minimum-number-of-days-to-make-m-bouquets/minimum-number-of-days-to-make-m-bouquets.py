class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n=len(bloomDay)
        if m*k>n:
            return -1
        def possible(bloomDay,day,m,k):
            cnt=0
            noOfB=0
            for i in range(n):
                if bloomDay[i]<=day:
                    cnt+=1
                else:
                    noOfB+=cnt//k
                    cnt=0
            noOfB+=cnt//k
            return noOfB>=m

        mini=float('inf')
        maxi=float('-inf')
        for i in range(n):
            mini=min(mini,bloomDay[i])
            maxi=max(maxi,bloomDay[i])
        low=mini
        high=maxi
        while low<=high:
            mid=(low+high)//2
            if possible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low    
