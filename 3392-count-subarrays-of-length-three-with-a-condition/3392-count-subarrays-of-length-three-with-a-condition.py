class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        for i in range(n - 2):
            if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
                answer += 1

        return answer