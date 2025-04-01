class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        answer, max_points = 0, 0
        for i, (point, brainpower) in enumerate(questions):
            max_points = max(max_points, dp[i])
            if i + brainpower + 1 < n:
                dp[i + brainpower + 1] = max(max_points + point, dp[i + brainpower + 1])
            
            answer = max(max_points + point, answer)
        return answer
