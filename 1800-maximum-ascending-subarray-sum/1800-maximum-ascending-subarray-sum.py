class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum = maximum_sum = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                sum += nums[i + 1]
            else:
                sum = nums[i + 1]
            maximum_sum = max(maximum_sum, sum)
        return maximum_sum