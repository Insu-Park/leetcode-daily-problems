class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return sum(f*(f-1)*4 for f in (Counter(x*y for x, y in combinations(nums, 2))).values() if f>1)