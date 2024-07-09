class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = 0
        now = 0
        for arrival, time in customers:
            if now < arrival:
                now = arrival
            else:
                waiting += now - arrival

            now += time
            waiting += time
        
        return waiting / len(customers)