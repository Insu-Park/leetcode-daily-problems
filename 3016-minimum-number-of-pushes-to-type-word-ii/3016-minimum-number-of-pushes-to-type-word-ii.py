class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(list(word)).values(), reverse=True)
        count = 0
        answer = 0
        for f in freq:
            answer += (count // 8 + 1) * f
            count += 1
        
        return answer
