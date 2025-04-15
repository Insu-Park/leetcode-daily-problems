class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n
        for i, val in enumerate(nums2):
            pos2[val] = i
        
        mapped = [pos2[val] for val in nums1]
        
        left = [0] * n
        sl = SortedList()
        for i in range(n):
            left[i] = sl.bisect_left(mapped[i])
            sl.add(mapped[i])
        
        right = [0] * n
        sl = SortedList()
        for i in reversed(range(n)):
            right[i] = len(sl) - sl.bisect_right(mapped[i])
            sl.add(mapped[i])
        
        total = sum(left[i] * right[i] for i in range(n))
        return total