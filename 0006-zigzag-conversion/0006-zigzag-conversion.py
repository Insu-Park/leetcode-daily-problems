class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        fixed_cols = numRows - 1
        repeat_strlen = 2 * numRows - 2
        iteration = (len(s) // repeat_strlen) + 1
        max_cols = iteration * fixed_cols
        lst = [[''] * max_cols for _ in range(numRows)]
        index, x, y = 0, 0, 0
        
        while index < len(s):
            lst[x][y] = s[index]
            if y % fixed_cols == 0 and x < numRows - 1:
                x += 1
            else:
                x -= 1
                y += 1
            index += 1
        
        answer = []
        for x in range(numRows):
            for y in range(max_cols):
                if lst[x][y] != '':
                    answer.append(lst[x][y])
        return "".join(answer)
