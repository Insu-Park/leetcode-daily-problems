class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        inf = float('inf')
        d = [[inf] * m for _ in range(n)]
        v = [[0] * m for _ in range(n)]
        d[0][0] = 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = []
        heapq.heappush(q, (0, 0, 0))  # (distance, x, y)
        while q:
            dis, x, y = heapq.heappop(q)
            if v[x][y]:
                continue
            if x == n - 1 and y == m - 1:
                break
            v[x][y] = 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                dist = max(d[x][y], moveTime[nx][ny]) + (x + y) % 2 + 1
                if d[nx][ny] > dist:
                    d[nx][ny] = dist
                    heapq.heappush(q, (dist, nx, ny))

        return d[n - 1][m - 1]