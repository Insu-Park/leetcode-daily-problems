class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        start, end = 0, 10 ** 14
        answer = end
        while start <= end:
            mid = (start + end) // 2
            can_repairs = 0
            for rank in ranks:
                can_repairs += math.floor(math.sqrt(mid / rank))
            
            if can_repairs >= cars:
                answer = min(answer, mid)
                end = mid - 1
            else:
                start = mid + 1

        return answer
