class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for item in arr:
            d[item] += 1
            if d[item] > len(arr) / 4:
                return item