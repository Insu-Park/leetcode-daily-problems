class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        answer = []
        s = set()
        for row in range(m):
            s.add(min(matrix[row]))

        for column in range(n):
            t = max([matrix[row][column] for row in range(m)])
            if t in s:
                answer.append(t)

        return answer