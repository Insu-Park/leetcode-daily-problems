class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        emptyBottles = 0
        while numBottles > 0:
            answer += numBottles
            numBottles += emptyBottles
            numBottles = numBottles // numExchange
            emptyBottles = numBottles % numExchange
        return answer