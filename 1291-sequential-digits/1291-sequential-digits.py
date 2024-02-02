class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = '123456789'
        seq_digits = []
        for i in range(0, 9):
            for j in range(i + 2, 10):
                seq_digits.append(int(nums[i:j]))
        
        seq_digits.sort()
        answer = []

        for i in seq_digits:
            if low <= i <= high:
                answer.append(i)

        return answer