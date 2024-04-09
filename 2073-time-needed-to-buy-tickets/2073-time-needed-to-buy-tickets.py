class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        v = tickets[k]
        for idx, ticket in enumerate(tickets):
            if idx <= k:
                answer += min(v, ticket)
            else:
                answer += min(v - 1, ticket)
        return answer

