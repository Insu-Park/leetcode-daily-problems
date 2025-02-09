class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        answer = n * (n - 1) // 2
        sum_dic = defaultdict(int)
        for i in range(n):
            sum_dic[nums[i] - i] += 1
            answer -= sum_dic[nums[i] - i] - 1
        
        return answer
        