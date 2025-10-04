class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket=defaultdict(int)
        left=0
        right=0
        maxlen=0
        n=len(fruits)
        while (right<n):
            basket[fruits[right]]+=1
            if len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1
            if  len(basket)<=2:
                maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen  