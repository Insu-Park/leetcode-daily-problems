class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        s = sorted(zip(difficulty, profit))
        dp = defaultdict(int)
        start = 0
        max_profit = 0
        for i in range(max(worker) + 1):
            if start < len(s) and i == s[start][0]:
                max_profit = max(max_profit, s[start][1])
                start += 1

            dp[i] = max_profit

        answer = 0
        for w in worker:
            answer += dp[w]
        return answer