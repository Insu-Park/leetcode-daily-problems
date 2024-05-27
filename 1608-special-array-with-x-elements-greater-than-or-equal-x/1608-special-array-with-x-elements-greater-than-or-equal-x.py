class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = max(nums)
        idx = 0
        for i in range(m + 1):
            print(i, idx, nums[idx])
            while idx < n and i > nums[idx]: idx += 1
            if i == n - idx:
                return i
        
        return -1