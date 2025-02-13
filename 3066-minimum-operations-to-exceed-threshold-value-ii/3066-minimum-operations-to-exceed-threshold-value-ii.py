class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        tmp = 0
        while nums[0] < k:
            count += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            tmp = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, tmp)

        return count