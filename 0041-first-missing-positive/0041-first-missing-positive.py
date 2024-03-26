class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        c = 1
        while c in s:
            c += 1
        return c 
