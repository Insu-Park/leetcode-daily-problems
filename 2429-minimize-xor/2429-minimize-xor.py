class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        answer = 0
        two_squares = [2 ** i for i in range(0, 31)][::-1]
        num = num1
        num1_count = 0
        num2_count = 0
        for i in two_squares:
            if num2 >= i:
                num2_count += 1
                num2 -= i
        
        positions = [0] * 31

        for idx, i in enumerate(two_squares):
            if num1 >= i:
                num1_count += 1
                num1 -= i
                positions[idx] = 1
                answer += i
                if num2_count == num1_count:
                    return answer
        
        diff = num2_count - num1_count
        for i, j in zip(positions[::-1], two_squares[::-1]):
            if i == 0:
                answer += j
                diff -= 1
            if diff == 0:
                break

        return answer
