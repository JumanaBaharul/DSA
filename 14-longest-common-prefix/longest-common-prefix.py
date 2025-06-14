class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        def isCommonPrefix(length):
            prefix=strs[0][:length]
            for string in strs:
                if not string.startswith(prefix):
                    return False
            return True
        low=0
        high=min(len(s) for s in strs)
        while low<=high:
            mid=(low+high)//2
            if isCommonPrefix(mid):
                low=mid+1
            else:
                high=mid-1
        return strs[0][:(low+high)//2]