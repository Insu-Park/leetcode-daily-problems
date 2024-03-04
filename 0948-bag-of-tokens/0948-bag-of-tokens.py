class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        deq = deque(sorted(tokens))
        score = 0
        while deq:
            if power >= deq[0]:
                power -= deq.popleft()
                score += 1
            else:
                if len(deq) > 2 and score:
                    power += deq.pop()
                    score -= 1
                else:
                    return score
                
        return score