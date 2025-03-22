class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = [0] * n
        root_data = defaultdict(int)
        
        def find_root(node):
            if parent[node] != node:
                parent[node] = find_root(parent[node])
            return parent[node]
        
        for start, stop in edges:
            source = find_root(start)
            target = find_root(stop)
            # print(parent)
            count[start] += 1
            count[stop] += 1


            if source != target:
                parent[source] = target
                root_data[target] += root_data[source] + 1
        
        except_count = 0
        roots = set()
        for node in parent:
            root = find_root(node)
            roots.add(root)
        
        was = set()

        for node in range(n):
            root = find_root(node)
            if root in was:
                continue
            if root_data[root] != count[node]:
                except_count -= 1
                was.add(root)

        return len(roots) + except_count