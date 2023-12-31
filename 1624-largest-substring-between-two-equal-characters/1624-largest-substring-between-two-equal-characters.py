class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1
        for idx in range(len(s)):
            start, end = s.find(s[idx]), s.rfind(s[idx])
            max_len = max(max_len, end - start - 1)
        return max_len