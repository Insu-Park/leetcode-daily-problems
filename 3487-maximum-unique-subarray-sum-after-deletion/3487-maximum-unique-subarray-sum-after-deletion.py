class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        answer = 0
        for num in nums:
            if num > 0 and num not in s:
                answer += num
                s.add(num)
        
        if answer == 0:
            return max(nums)

        return answer