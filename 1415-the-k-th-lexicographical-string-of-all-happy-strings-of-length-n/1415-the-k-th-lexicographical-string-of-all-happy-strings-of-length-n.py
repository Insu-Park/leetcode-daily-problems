class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        answer = ""
        val = 0

        def backtrack(happy_str):
            nonlocal answer, val
            if len(happy_str) == n:
                val = val + 1
                if val == k:
                    answer = happy_str
                
                return val

            for i in range(3):
                ch = chr(ord('a') + i)
                if happy_str == "" or happy_str[-1] != ch:
                    backtrack(happy_str + ch)

                    if answer is not "":
                        return
            
            
        backtrack("")
        return answer