class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(int)
        for s, e in roads:
            d[s] += 1
            d[e] += 1
        
        t = sorted(d.items(), key=lambda x: x[1], reverse=True)
        answer = 0

        for k, v in t:
            answer += n * v
            n -= 1

        return answer
