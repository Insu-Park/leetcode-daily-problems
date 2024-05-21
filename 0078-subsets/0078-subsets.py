class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums) + 1):
            for items in list(combinations(nums, i)):
                answer.append(items)
        
        return answer