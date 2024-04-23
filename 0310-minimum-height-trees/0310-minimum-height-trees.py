class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        conn = defaultdict(list)
        degrees = [0] * n

        for a, b in edges:
            conn[a].append(b)
            conn[b].append(a)
            degrees[a] += 1
            degrees[b] += 1

        queue = deque()
        for i in range(n):
            if degrees[i] == 1:
                queue.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            size = len(queue)
            remaining_nodes -= size
            
            for _ in range(size):
                leaf = queue.popleft()
                for neighbor in conn[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        
        return list(queue)
                
            
