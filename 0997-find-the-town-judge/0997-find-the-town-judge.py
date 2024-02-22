class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        everybody = [0] * (n + 1)
        town_judge = [0] * (n + 1)
        for a, b in trust:
            everybody[a] += 1
            town_judge[b] += 1
        for i in range(1, n + 1):
            if town_judge[i] == n - 1 and everybody[i] == 0:
                return i
        return -1
