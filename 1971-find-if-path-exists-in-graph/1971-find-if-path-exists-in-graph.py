class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        answer = False
        checked = [False] * n
        graph = defaultdict(list)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(node):
            nonlocal answer, checked, graph
            checked[node] = True
            for n in graph[node]:
                if not checked[n]:
                    if n == destination:
                        answer = True
                    else:
                        dfs(n)
            
        dfs(source)
        return answer