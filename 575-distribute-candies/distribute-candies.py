class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        unique=set(candyType)

        if len(unique)<n//2:
            return len(unique)
        else:
            return n//2