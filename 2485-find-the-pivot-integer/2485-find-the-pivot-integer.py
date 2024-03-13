class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 0, (n + 1) * n // 2
        for i in range(1, n + 1):
            right -= i
            pivot = i
            if left == right: 
                return pivot
            elif left > right:
                return -1
        
            left += i
        return -1