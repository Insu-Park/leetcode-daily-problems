class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def findLetter(used, idx, x, y):
            if idx == len(word):
                return True
            else:
                if x < n - 1 and not used[x + 1][y] and board[x + 1][y] == word[idx]:
                    used[x + 1][y] = True
                    if findLetter(used, idx + 1, x + 1, y): return True
                    used[x + 1][y] = False
                if x > 0 and not used[x - 1][y] and board[x - 1][y] == word[idx]:
                    used[x - 1][y] = True
                    if findLetter(used, idx + 1, x - 1, y): return True
                    used[x - 1][y] = False
                if y < m - 1 and not used[x][y + 1] and board[x][y + 1] == word[idx]:
                    used[x][y + 1] = True
                    if findLetter(used, idx + 1, x, y + 1): return True
                    used[x][y + 1] = False
                if y > 0 and not used[x][y - 1] and board[x][y - 1] == word[idx]:
                    used[x][y - 1] = True
                    if findLetter(used, idx + 1, x, y - 1): return True
                    used[x][y - 1] = False
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    used = [[False] * m for _ in range(n)]
                    used[i][j] = True
                    if findLetter(used, 1, i, j): return True
        
        return False