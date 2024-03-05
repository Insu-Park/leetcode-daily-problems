class Solution:
    def minimumLength(self, s: str) -> int:
        answer = deque(s)
        while len(answer) > 1 and answer[0] == answer[-1]:
            c = answer[0]
            while answer and c == answer[0]: answer.popleft()
            while answer and c == answer[-1]: answer.pop()
        
        return len(answer)