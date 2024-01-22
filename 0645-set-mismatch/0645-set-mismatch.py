class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        errors = [0, 0]
        for num in nums:
            if num in s:
                errors[0] = num
            else:
                s.add(num)
        
        for idx in range(1, len(nums) + 1):
            if idx not in s:
                errors[1] = idx
                return errors

