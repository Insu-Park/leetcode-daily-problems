class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        moves=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        @cache
        def dfs(x, y, moveLeft):
            if x < 0 or x == m or y < 0 or y == n: return 1
            if moveLeft == 0: return 0
            answer = 0
            for a, b in moves:
                answer = (answer + dfs(x + a, y + b, moveLeft-1)) % MOD
            return answer
        return dfs(startRow, startColumn, maxMove)