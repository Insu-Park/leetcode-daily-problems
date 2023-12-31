class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        alphabets = set(s)
        max_len = -1
        s_len = len(s) 
        for alphabet in alphabets:
            start, end = s.find(alphabet), len(s) - s[::-1].find(alphabet) - 1
            if start != end:
                max_len = max(max_len, end - start - 1)
        return max_len