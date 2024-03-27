class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        start, end, answer, product = 0, 0, 0, 1
        while end < len(nums):
            product *= nums[end]
            while product >= k:
                product //= nums[start]
                start += 1
            answer += 1 + (end - start)
            end += 1

        return answer