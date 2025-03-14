class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        answer = 0
        left, right = 0, sum(candies) // k
        while left < right:
            mid = (left + right) // 2
            print(left, right, mid)

            piles = 0
            for candy in candies:
                piles += candy // mid
            
            if piles >= k:
                answer = max(answer, mid)
                left = mid + 1
            else:
                right = mid

        return answer