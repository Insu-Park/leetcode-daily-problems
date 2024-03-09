class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        commons = set(nums1) & set(nums2)
        if commons: return min(commons)
        return -1