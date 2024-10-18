class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda a, b: a | b, nums)
        return self.dfs(nums, 0, 0, max_or)
    def dfs(self, nums, i, or_val, max_or):
        return (or_val == max_or) if i == len(nums) else self.dfs(nums, i + 1, or_val | nums[i], max_or) + self.dfs(nums, i + 1, or_val, max_or)