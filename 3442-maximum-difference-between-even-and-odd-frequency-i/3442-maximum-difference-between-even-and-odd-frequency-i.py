class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        a1, a2 = 0, 0
        for k, v in c.items():
            if v % 2 == 0:
                if a2 == 0:
                    a2 = v
                else:
                    a2 = min(a2, v)
            else:
                a1 = max(a1, v)
        
        return a1 - a2