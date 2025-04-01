class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        answer = 0
        for i, (point, brainpower) in enumerate(questions):
            if i + brainpower + 1 < n:
                dp[i + brainpower + 1] = dp[i] + point
            
            answer = max(dp[i] + point, answer)
        return answer
