class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d, ch = {}, set()
        for a, b in zip(s, t):
            if a not in d and b not in ch:
                d[a] = b
                ch.add(b)
            elif a not in d and b in ch:
                return False
            elif d[a] != b:
                return False
        return True