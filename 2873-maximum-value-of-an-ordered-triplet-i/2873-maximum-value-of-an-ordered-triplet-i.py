class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]: continue
                for k in range(j + 1, n):
                    answer = max((nums[i] - nums[j]) * nums[k], answer)
        
        return answer