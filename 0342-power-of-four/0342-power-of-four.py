class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        s = set([4 ** x for x in range(16)])
        return n in s