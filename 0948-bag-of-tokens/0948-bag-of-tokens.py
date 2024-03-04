class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        deq = deque(sorted(tokens))
        max_score = score = 0
        while deq:
            if power >= deq[0]:
                power -= deq.popleft()
                score += 1
            else:
                if score > 0:
                    power += deq.pop()
                    max_score = score
                    score -= 1
                else: return 0
                
        return max(max_score, score)