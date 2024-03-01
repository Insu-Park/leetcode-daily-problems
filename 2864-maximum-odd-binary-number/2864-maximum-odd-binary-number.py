class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = 0
        ans = ['1'] * len(s)
        for c in s:
            if c == '0':
                zeros += 1
        
        for z in range(1, zeros + 1):
            ans[z] = '0'

        return "".join(ans[::-1])
