class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = sorted(Counter(nums).items())
        answer = 0
        last_key, last_value = c[0]


        for k, v in c[1:]:
            if k - last_key == 1:
                answer = max(answer, last_value + v)
            last_key, last_value = k, v
            print(last_key, last_value, answer)
        return answer