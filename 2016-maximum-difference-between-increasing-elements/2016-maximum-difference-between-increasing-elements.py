class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - min_val > 0:
                answer = max(answer, nums[i] - min_val)
            min_val = min(min_val, nums[i])

        return answer