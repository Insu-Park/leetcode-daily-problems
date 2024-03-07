class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(longest) > (j - i): continue
                start, end = i, j
                while end - start > 1 and s[start] == s[end - 1]:
                    start += 1
                    end -= 1
                if end - start <= 1:
                    longest = longest if len(longest) > len(s[i:j]) else s[i:j]
        return longest
