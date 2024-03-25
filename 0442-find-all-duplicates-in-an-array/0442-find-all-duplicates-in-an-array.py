class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        answer = []
        for num in nums:
            if num in s:
                answer.append(num)
            else:
                s.add(num)
        return answer