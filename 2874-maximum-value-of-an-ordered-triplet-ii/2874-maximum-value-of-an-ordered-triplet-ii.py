class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        high, diff, answer = 0, 0, 0
        for num in nums:
            answer = max(answer, diff * num)
            diff = max(high - num, diff)
            high = max(high, num)
        return answer