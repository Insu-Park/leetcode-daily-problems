class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        first, second = 1, 1
        answer = 0
        for i in range(1, n):
            answer = first + second
            first, second = second, answer

        return answer