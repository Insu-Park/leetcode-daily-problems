class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        answer = 0
        for v in nums_dict.values():
            if v == 1:
                return -1
            else:
                answer += math.ceil(v / 3)
        return answer      
