class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        answer = 0
        e = defaultdict(list)
        for idx, (s, d) in enumerate(edges):
            e[s].append([d, succProb[idx]])
            e[d].append([s, succProb[idx]])
            

        def dfs(node, visited, p):
            nonlocal answer
            if node == end_node:
                answer = max(answer, p)
            
            for n, sp in e[node]:
                if n not in visited:
                    dfs(n, visited.union(set([n])), p * sp)
        
        dfs(start_node, set(), 1)
        return answer