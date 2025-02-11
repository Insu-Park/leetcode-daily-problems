class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        answer = []
        part = list(part)
        n = len(part)
        m = n * (-1)
        for c in s:
            answer.append(c)
            if len(answer) >= n and answer[m:] == part:
                for i in range(n):
                    answer.pop()
        
        return "".join(answer)
