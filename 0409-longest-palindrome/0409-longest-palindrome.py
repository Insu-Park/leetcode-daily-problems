class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        answer, odds = 0, 0
        for key, value in c.items():
            if value % 2 == 1: odds += 1 
            answer += value

        if odds != 0: answer = answer - odds + 1
        return answer