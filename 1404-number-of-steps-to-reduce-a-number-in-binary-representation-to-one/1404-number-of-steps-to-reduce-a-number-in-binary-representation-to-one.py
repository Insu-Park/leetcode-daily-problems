class Solution:
    def numSteps(self, s: str) -> int:
        multiple = 1
        num = 0
        for c in s[::-1]:
            num += int(c) * multiple
            multiple *= 2
        
        count = 0
        while num > 1:
            if num % 2 == 0: num //= 2
            else: num += 1
            count += 1
        return count
