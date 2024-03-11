class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x >= 0 else -1
        x = int(str(x * flag)[::-1]) * flag
        if (2 ** 31) * (-1) <= x <= (2 ** 31) - 1:    
            return x
        return 0