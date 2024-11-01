class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = []
        for i, c in enumerate(s):
            if i >= 2 and s[i - 2] == s[i - 1] and s[i - 1] == c:
                continue
            answer.append(c)
        
        return "".join(answer)