class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        first_row_sum, second_row_sum = sum(grid[0][i] for i in range(1, n)), 0
        min_value = first_row_sum
        for i in range(1, n):
            first_row_sum -= grid[0][i]
            second_row_sum += grid[1][i - 1]
            min_value = min(min_value, max(first_row_sum, second_row_sum))

        return min_value