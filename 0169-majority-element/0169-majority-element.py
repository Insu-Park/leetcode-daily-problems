class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(c.keys(), key=lambda k: c[k])