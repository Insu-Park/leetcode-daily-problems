class Solution:
    def maxDepth(self, s: str) -> int:
        now, max_depth = 0, 0
        for c in s:
            if c == '(':
                now += 1
            elif c == ')':
                now -= 1
            max_depth = max(max_depth, now)
        return max_depth