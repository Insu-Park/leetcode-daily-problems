class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ret = [[0] * n for _ in range(n)]
        for x in range(n - 1):
            tmp = [0] * (x + 1)
            i = x
            j = n - 1
            k = 0
            while i >= 0 and j >= 0:
                tmp[k] = grid[i][j]
                i -= 1
                j -= 1
                k += 1

            tmp.sort(reverse=True)
            i = x
            j = n - 1
            k = 0
            while i >= 0 and j >= 0:
                ret[i][j] = tmp[k]
                i -= 1
                j -= 1
                k += 1

        for y in range(n - 1, -1, -1):
            tmp = [0] * (y + 1)
            i = n - 1
            j = y
            k = 0
            while i >= 0 and j >= 0:
                tmp[k] = grid[i][j]
                i -= 1
                j -= 1
                k += 1

            tmp.sort()
            i = n - 1
            j = y
            k = 0
            while i >= 0 and j >= 0:
                ret[i][j] = tmp[k]
                i -= 1
                j -= 1
                k += 1

        return ret