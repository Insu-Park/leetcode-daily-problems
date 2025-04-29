class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        start, end, answer = 0, 0, 0
        while end < n:
            if nums[end] == m:
                k -= 1
            
            end += 1
            while k == 0:
                if nums[start] == m:
                    k += 1
                start += 1
            answer += start
        return answer
        