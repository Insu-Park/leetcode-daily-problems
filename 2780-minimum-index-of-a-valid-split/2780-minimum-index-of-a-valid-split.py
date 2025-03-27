class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        x, nums_x = 0, 0
        for item, value in counter.items():
            if x < value:
                x, nums_x = item, value

        left_x = 0
        for i in range(n):
            if nums[i] == x:
                left_x += 1
            
            if left_x * 2 > (i + 1) and (nums_x - left_x) * 2 > n - i - 1:
                return i

        return -1