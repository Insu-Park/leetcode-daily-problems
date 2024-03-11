class Solution:
    def customSortString(self, order: str, s: str) -> str:
        answer = []
        for o in order:
            for c in s:
                if o == c:
                    answer.append(c)
        
        for c in s:
            if c not in order:
                answer.append(c)

        return "".join(answer)