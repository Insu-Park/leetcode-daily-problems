class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1
        used = set()
        answer = ""

        def backtrack(di, used):
            nonlocal answer
            l = len(di)
            if n == l:
                answer = min(answer, di) if answer is not "" else di
                return
            
            for i in range(1, 10):
                if i in used:
                    continue

                if di == "" or (pattern[l - 1] == "I" and di[-1] < str(i)) or (pattern[l - 1] == "D" and di[-1] > str(i)):
                    used.add(i)
                    backtrack(di + str(i), used)
                    used.remove(i)
        
        backtrack("", used)
        return answer

                