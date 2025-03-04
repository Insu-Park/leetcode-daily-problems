class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 1:
            if n % 3 != 0:
                n -= 1
            if n % 3 != 0:
                return False
            n = n // 3
                
        return True