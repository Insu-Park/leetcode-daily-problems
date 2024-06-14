class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        prev = nums[0]

        for num in nums[1:]:
            if num <= prev:
                prev += 1
                answer += prev - num
            else:
                prev = num

        return answer