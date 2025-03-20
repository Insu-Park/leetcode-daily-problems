class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        # 그래프 생성 (무방향)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        parent = list(range(n))
        min_and_cost = [0xFFFFFFFF] * n  # 각 컴포넌트에서의 최소 AND 비용
        
        # 유니온-파인드 (경로 압축)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y, w):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
                min_and_cost[root_x] &= min_and_cost[root_y]  # 기존 최소 비용 병합
            min_and_cost[root_x] &= w  # 새로운 간선 비용 반영

        # BFS를 활용하여 컴포넌트별 최소 AND 값 계산
        visited = set()
        for node in range(n):
            if node not in visited:
                queue = deque([node])
                visited.add(node)
                and_cost = 0xFFFFFFFF
                nodes_in_component = []
                
                while queue:
                    curr = queue.popleft()
                    nodes_in_component.append(curr)
                    
                    for neighbor, weight in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                        union(curr, neighbor, weight)
                        and_cost &= weight  # 현재 컴포넌트의 최소 AND 갱신
                
                # 모든 노드에 최소 비용 반영
                root = find(node)
                for comp_node in nodes_in_component:
                    min_and_cost[comp_node] = and_cost

        # 쿼리 처리
        result = []
        for u, v in query:
            if find(u) != find(v):
                result.append(-1)  # 다른 컴포넌트에 속하면 이동 불가
            else:
                result.append(min_and_cost[find(u)])  # 같은 컴포넌트라면 최소 비용 반환
        
        return result