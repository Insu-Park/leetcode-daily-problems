class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        return None

    def add(self, val: int) -> int:
        if not self.heap:
            heapq.heappush(self.heap, val)
        
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)