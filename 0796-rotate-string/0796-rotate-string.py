class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        if len(s) != len(goal) or len(s) == 1:
            return False
        if Counter(s) != Counter(goal):
            return False
        
        s, g = list(s), list(goal)
        for i in range(len(s)):
            t = s.pop(0)
            s.append(t)
            if s == g:
                return True
        
        return False 