class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        new_mat = [[0] * m for i in range(n)]
        answer = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_mat[j][i] = mat[i][j]

        for i in range(len(mat)):
            if mat[i].count(1) == 1 and new_mat[mat[i].index(1)].count(1) == 1:
                answer += 1
        return answer 