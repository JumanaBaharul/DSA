class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cnt=0
        maxi=0
        for sentence in sentences:
            cnt=len(sentence.split())
            maxi=max(maxi,cnt)
        return maxi