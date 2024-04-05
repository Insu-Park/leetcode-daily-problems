class Solution:
    def makeGood(self, s: str) -> str:
        idx = 0
        while idx + 1 < len(s):
            if s[idx].upper() == s[idx + 1] or s[idx] == s[idx + 1].upper():
                s = s[:idx] if idx + 2 >= len(s) else s[:idx] + s[idx + 2:]
                idx = 0
            else:
                idx += 1
        
        return s
