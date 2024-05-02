class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for num in nums[::-1]:
            if (num * -1) in nums:
                return num

        else: return -1