class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid2), len(grid2[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid2[i][j] == 0:
                return
            if grid1[i][j] != 1:
                nonlocal flag
                flag = False
            grid2[i][j] = 0  # Mark cell as visited
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:
                    flag = True
                    dfs(i, j)
                    if flag:
                        count += 1
        
        return count