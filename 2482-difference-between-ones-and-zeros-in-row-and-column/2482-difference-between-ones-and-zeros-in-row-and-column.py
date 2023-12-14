class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diff = [[0] * n for i in range(m)]
        row_one_count, col_one_count = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                row_one_count[i] += grid[i][j]
                col_one_count[j] += grid[i][j]
        
        for i in range(m):
            for j in range(n):
                diff[i][j] = row_one_count[i] * 2 + col_one_count[j] * 2 - m - n
            
        return diff