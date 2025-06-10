class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        n=len(weights)
        def findDays(weights,capacity):
            days=1
            load=0
            for i in range(n):
                if load+weights[i]>capacity:
                    days+=1
                    load=weights[i]
                else:
                    load+=weights[i]
            return days
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            if findDays(weights,mid)<=days:
                high=mid-1
            else:
                low=mid+1
        return low