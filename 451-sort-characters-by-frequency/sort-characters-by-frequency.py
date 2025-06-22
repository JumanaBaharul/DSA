class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        max_freq=max(freq.values())
        buckets=[[] for _ in range(max_freq+1)]
        for char,count in freq.items():
            buckets[count].append(char)
        result=[]
        for i in range(len(buckets)-1,0,-1):
            for char in buckets[i]:
                result.append(char*i)
        return ''.join(result)