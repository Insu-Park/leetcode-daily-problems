class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        answer = 0
        i = 0
        max_day = max(i[1] for i in events)
        for day in range(1, max_day + 1):
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(pq, events[i][1])
                i += 1
            while pq and day > pq[0]:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                answer += 1
        return answer