class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives, zeros = 0, 0
        for num in nums:
            if num < 0:
                negatives += 1
            elif num == 0:
                zeros += 1
            else:
                break
        return max(negatives, len(nums) - negatives - zeros)