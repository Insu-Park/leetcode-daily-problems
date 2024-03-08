class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_frequency = max(c.values())
        return list(c.values()).count(max_frequency) * max_frequency
