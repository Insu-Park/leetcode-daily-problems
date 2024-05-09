class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        answer = 0
        count = 0
        while k > 0:
            v = happiness.pop() - count
            if v <= 0:
                break
            answer += v
            count += 1
            k -= 1
        
        return answer