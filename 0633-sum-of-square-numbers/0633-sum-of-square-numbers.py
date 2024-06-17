class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        squares = []
        while i * i <= c:
            squares.append(i * i)
            i += 1

        s = set(squares)
        for i in squares:
            if (c - i) in s:
                return True

        return False
