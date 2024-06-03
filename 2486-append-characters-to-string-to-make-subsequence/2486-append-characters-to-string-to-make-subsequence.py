class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx = 0
        for c in s:
            if idx < len(t) and c == t[idx]: idx += 1
        
        return len(t) - idx