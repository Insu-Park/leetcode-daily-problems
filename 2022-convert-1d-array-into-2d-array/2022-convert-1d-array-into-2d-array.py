class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        idx = 0
        arr = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                arr[i][j] = original[idx]
                idx += 1
        
        return arr