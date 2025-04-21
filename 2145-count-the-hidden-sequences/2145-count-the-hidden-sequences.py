class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences) + 1
        start = 0
        diffs = [0] * n
        for i in range(n - 1):
            diffs[i + 1] = diffs[i] + differences[i]

        max_d, min_d = max(diffs), min(diffs)
        answer = (upper - lower) - (max(diffs) - min(diffs)) + 1
        return answer if answer > 0 else 0

