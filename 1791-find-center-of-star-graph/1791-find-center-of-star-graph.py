class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s = set()
        for u, v in edges:
            if u in s: return u
            if v in s: return v
            s.add(u)
            s.add(v)
        return 0