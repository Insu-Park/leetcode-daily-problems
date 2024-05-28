class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        answer = 0
        subs = [0] * n
        cost = 0
        start = 0
        for i in range(n):
            subs[i] = abs(ord(s[i]) - ord(t[i]))
            cost += subs[i]
            while cost > maxCost:
                cost -= subs[start]
                start += 1
            answer = max(answer, i - start + 1)

        return answer
