class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        digit = len(nums)
        fm = "{:0" + str(digit) + "d}"
        for i in range(2 ** digit):
            num = fm.format(int(format(i, 'b')))
            if num not in s:
                return num
        