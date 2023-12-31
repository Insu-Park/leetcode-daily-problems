class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        alphabets = set(s)
        max_len = -1
        for alphabet in alphabets:
            start, end = s.find(alphabet), s.rfind(alphabet)
            max_len = max(max_len, end - start - 1)
        return max_len