class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            curr = grid[i][j]
            grid[i][j] = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if -1 < x < m and -1 < y < n and grid[x][y] != 0:
                    curr += dfs(x, y)
            return curr

        res = float('-inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j))

        return max(res, 0)