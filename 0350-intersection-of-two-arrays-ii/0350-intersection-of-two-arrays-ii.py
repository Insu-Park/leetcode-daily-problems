class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        answer = []
        for k, v in c1.items():
            if k in c2.keys():
                min_v = min(c1[k], c2[k])
                for _ in range(min_v):
                    answer.append(k)
        
        return answer