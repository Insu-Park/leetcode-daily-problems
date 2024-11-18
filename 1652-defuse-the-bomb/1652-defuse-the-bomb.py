class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        answer = [0] * n
        for i in range(n):
            if k > 0:
                for j in range(k):
                    answer[i] += code[(i + j + 1) % n]
                     
            elif k < 0:
                for j in range(0, k, -1):
                    answer[i] += code[i + j - 1]
        
        return answer