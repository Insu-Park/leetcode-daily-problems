class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        deq = deque([i for i in range(n)])

        while len(deq) > 1:
            for _ in range(k - 1):
                t = deq.popleft()
                deq.append(t)

            deq.popleft()
        
        return deq[0] + 1
