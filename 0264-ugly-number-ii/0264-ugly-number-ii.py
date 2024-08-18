class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = set([2, 3, 5])
        for i in range(30):
            copy = list(s)
            for item in copy:
                s.add(item * 2)
                s.add(item * 3)
                s.add(item * 5)
        
        s.add(1)
        sorted_s = sorted(list(s))
        return sorted_s[n - 1]