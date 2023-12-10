class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        answer = [[0] * m for i in range(n)]
        for i, it in enumerate(matrix):
            for j, jt in enumerate(it):
                answer[j][i] = jt
        return answer