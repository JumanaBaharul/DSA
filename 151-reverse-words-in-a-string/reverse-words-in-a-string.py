class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        temp = ""

        for ch in s:
            if ch != " ":
                temp += ch
            else:
                if temp:
                    words.append(temp)
                    temp = ""
        
        if temp:
            words.append(temp)

        return " ".join(reversed(words))