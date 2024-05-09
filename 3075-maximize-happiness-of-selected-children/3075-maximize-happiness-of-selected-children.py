class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        answer = 0
        count = 0
        while k > 0:
            answer += max(0, happiness.pop() - count)
            count += 1
            k -= 1
        
        return answer