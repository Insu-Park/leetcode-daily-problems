class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ret, max_d = 0, 0
        for d in dimensions:
            if max_d <= d[0] ** 2 + d[1] ** 2:
                if max_d == d[0] ** 2 + d[1] ** 2:
                    ret = max(ret, d[0] * d[1])
                else:    
                    max_d = d[0] ** 2 + d[1] ** 2
                    ret = d[0] * d[1]


        return ret