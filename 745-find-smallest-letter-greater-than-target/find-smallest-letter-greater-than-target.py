class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:        
        smallest=float('inf')

        for ch in letters:
            if ord(ch)>ord(target):
                smallest=min(smallest,ord(ch))

        if smallest==float('inf'):
            return letters[0]

        return chr(smallest) 