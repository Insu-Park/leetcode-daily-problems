class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        answer = False
        checked = [False] * n
        checked[source] = True

        graph = defaultdict(list)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)


        def dfs(node, graph):
            nonlocal answer, checked
            if node == destination:
                return True

            checked[node] = True
            for n in graph[node]:
                if not checked[n] and dfs(n, graph):
                    answer = True
            
            return False

        dfs(source, graph)
        return answer