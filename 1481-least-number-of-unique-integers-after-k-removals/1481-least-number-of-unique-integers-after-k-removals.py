class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums = Counter(arr).most_common()
        idx = 0

        for key, value in nums[::-1]:
            if k >= value:
                k -= value
                idx += 1
            else:
                break

        return len(nums) - idx