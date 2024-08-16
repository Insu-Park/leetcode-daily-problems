class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_heap, max_heap = [], []
        for idx, array in enumerate(arrays):
            heapq.heappush(min_heap, [array[0], idx])
            heapq.heappush(max_heap, [-1 * array[-1], idx])
        
        min1, min_idx = heapq.heappop(min_heap)
        max1, max_idx = heapq.heappop(max_heap)
        max1 *= -1
        if min_idx == max_idx:
            min2 = heapq.heappop(min_heap)[0]
            max2 = heapq.heappop(max_heap)[0]
            return max(max1 - min2, max2 - min1)
        
        return max1 - min1
