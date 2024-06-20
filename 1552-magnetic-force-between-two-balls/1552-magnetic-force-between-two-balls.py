class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        start = 1
        end = (position[-1] - position[0])
        ans = - 1
        while start <= end:
            mid = (start + end) // 2
            ball = position[0]
            num = 1

            for i in range(1, len(position)):
                if position[i] - ball >= mid:
                    ball = position[i]
                    num += 1

            if num >= m:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        
        return ans
        