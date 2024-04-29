class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = k
        for num in nums:
            res ^= num

        cnt = 0
        while res:
            res &= res - 1
            cnt += 1
        
        return cnt
