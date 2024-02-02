class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = '123456789'
        seq_digits = []
        for i in range(0, 9):
            for j in range(i + 2, 10):
                t = int(nums[i:j])
                if low <= t <= high:
                    seq_digits.append(t)
        
        return sorted(seq_digits)