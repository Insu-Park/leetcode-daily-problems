class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [[0] * (target + k + 1) for _ in range(n + 1)]
        for i in range(1, k + 1):
            dp[1][i] = 1

        for i in range(1, n):
            for j in range(1, target):
                for t in range(1, k + 1):
                    dp[i + 1][j + t] += dp[i][j] % modulo

        print(dp)
        return dp[n][target] % modulo