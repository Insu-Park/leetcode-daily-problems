class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        dp[0] = [grid[0][num] for num in range(n)]
        for i in range(1, n):
            s = deque(dp[i - 1])
            for j in range(n):
                s.popleft()
                dp[i][j] = min(s) + grid[i][j]
                s.append(dp[i - 1][j])

        return min(dp[n - 1])