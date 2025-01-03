class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        acc, cnt = 0, 0
        for i in range(n - 1):
            acc += nums[i]
            cnt += (2 * acc >= s)
        return cnt