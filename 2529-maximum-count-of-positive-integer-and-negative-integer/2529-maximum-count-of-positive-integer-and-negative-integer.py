class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positives, negatives = 0, 0
        for num in nums:
            if num > 0:
                positives += 1
            elif num < 0:
                negatives += 1
        return max(positives, negatives)