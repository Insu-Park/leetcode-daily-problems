class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            insert_index = bisect.bisect_left(dp, n)
            if insert_index == len(dp):
                dp.append(n)
            else:
                dp[insert_index] = n
        
        return len(dp)