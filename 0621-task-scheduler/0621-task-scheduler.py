class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        time = 0
        d = defaultdict(list)
        c = Counter(tasks)
        
        for task, left in c.items():
            heapq.heappush(heap, [left * -1, left, task]) 
        
        lefttasks = len(heap)

        while lefttasks > 0:
            if heap:
                _, left, task = heapq.heappop(heap)
                if left > 1:
                    d[time + n].append([task, left - 1])
                else:
                    lefttasks -= 1

            if d[time]:
                for task, left in d[time]:
                    heapq.heappush(heap, [left * -1, left, task])

            time += 1

        return time