class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken=set(brokenLetters)
        cnt=0
        for word in text.split():
            if all(char not in broken for char in word):
                cnt+=1
        return cnt