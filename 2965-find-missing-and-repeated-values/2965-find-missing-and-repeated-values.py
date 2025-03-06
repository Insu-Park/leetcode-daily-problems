class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n, s = len(grid), set()
        nn = n ** 2
        a, b = 0, 0
        sum = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in s:
                    s.add(grid[i][j])
                    sum += grid[i][j]
                else:
                    a = grid[i][j]

        b = ((nn + 1) * nn // 2) - sum
        return [a, b]