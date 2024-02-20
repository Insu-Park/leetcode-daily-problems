class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m, s, l = 0, 0, len(nums)
        for num in nums:
            s += num
            m = m if m > num else num

        if l == m + 1:
            return l

        return (m * (l + 1)) // 2 - s