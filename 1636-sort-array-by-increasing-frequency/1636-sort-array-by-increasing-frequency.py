class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0]))
        answer = []
        for num, it in nums:
            answer += [num] * it
        return answer