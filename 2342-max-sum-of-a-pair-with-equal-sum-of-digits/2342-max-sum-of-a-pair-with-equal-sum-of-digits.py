class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for num in nums:
            sum_of_digit = 0
            tmp = num
            while tmp > 0:
                sum_of_digit += tmp % 10
                tmp //= 10
            d[sum_of_digit].append(num)
        
        answer = -1
        for k in d.keys():
            if len(d[k]) >= 2:
                sorted_nums = sorted(d[k], reverse=True)
                answer = max(answer, sorted_nums[0] + sorted_nums[1])
        
        return answer