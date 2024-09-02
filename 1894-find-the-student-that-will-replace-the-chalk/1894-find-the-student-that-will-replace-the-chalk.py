class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for i, c in enumerate(chalk):
            k -= c
            if k < 0:
                return i