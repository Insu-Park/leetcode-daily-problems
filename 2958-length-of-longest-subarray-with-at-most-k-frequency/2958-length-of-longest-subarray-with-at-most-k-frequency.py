class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        start, end, count, answer = 0, 0, 0, 0
        
        while end < len(nums):
            count += 1
            d[nums[end]] += 1
            
            while d[nums[end]] > k:
                d[nums[start]] -= 1
                count -= 1
                start += 1

            answer = max(answer, count)
            end += 1
        return answer
