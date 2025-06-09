class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n=len(piles)
        def findMax(piles):
            maxi=float('-inf')
            for i in range(n):
                maxi=max(maxi,piles[i])
            return maxi
        def totaHours(piles,k):
            totalH=0
            for i in range(n):
                totalH+=math.ceil(float(piles[i])/k)
            return totalH
        low=1
        high=findMax(piles)
        while low<=high:
            mid=(low+high)//2
            totalH=totaHours(piles,mid)
            if totalH<=h:
                high=mid-1
            else:
                low=mid+1
        return low