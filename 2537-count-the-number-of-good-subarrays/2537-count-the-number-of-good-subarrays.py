class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = count = start = end = 0
        d = defaultdict(int)
        while start < n:
            while end < n and count < k:
                d[nums[end]] += 1
                if d[nums[end]] >= 2:
                    count += d[nums[end]] - 1
                end += 1

            if count < k:
                break
            
            answer += n - end + 1
            count -= d[nums[start]] - 1
            d[nums[start]] -= 1
            start += 1
        
        return answer
            
