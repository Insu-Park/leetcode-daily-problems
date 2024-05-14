class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        answer = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0: continue
                q = deque([[row, col, 0, 0, [[False] * n for _ in range(m)]]])
                while q:
                    x, y, val, step, visited = q.popleft()
                    if x < 0 or x >= m or y < 0 or y >= n: continue 
                    if not visited[x][y] and grid[x][y] != 0:
                        new_visited = [row[:] for row in visited]  # Create a new visited array
                        new_visited[x][y] = True
                        val += grid[x][y]
                        answer = max(answer, val)
                        q.append([x - 1, y, val, step + 1, new_visited])
                        q.append([x + 1, y, val, step + 1, new_visited])
                        q.append([x, y - 1, val, step + 1, new_visited])
                        q.append([x, y + 1, val, step + 1, new_visited])   
                                     
        return answer
                        