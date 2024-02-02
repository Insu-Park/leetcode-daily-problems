class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        seq_digits = []
        for i in range(0, 9):
            for j in range(i + 2, 10):
                seq_digits.append(int(''.join(nums[i:j])))
        
        seq_digits.sort()
        answer = []

        for i in seq_digits:
            if low <= i <= high:
                answer.append(i)

        return answer