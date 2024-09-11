class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        exp = start ^ goal
        while exp:
            exp &= exp - 1
            cnt += 1
        return cnt