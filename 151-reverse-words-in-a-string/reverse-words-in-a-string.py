class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        n = len(s)

        while i < n:
            while i < n and s[i] == " ":
                i += 1
            
            start = i
            
            while i < n and s[i] != " ":
                i += 1
            
            if start < i:
                words.append(s[start:i])

        return " ".join(reversed(words))