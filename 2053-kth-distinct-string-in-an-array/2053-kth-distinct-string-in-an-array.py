class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        count = 0
        for key, value in c.items():
            if value == 1:
                count += 1
            if count == k:
                return key

        return ""