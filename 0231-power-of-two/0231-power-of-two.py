class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powers = [2 ** p for p in range(31)]
        return n in powers
