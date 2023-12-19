import math 

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        new_img = [[0] * n for _ in range(m)]
        for i, row in enumerate(img):
            for j, col in enumerate(row):
                new_img[i][j] = self.get_average(img, i, j, m, n)
        return new_img

    def get_average(self, img: List[List[int]], i, j, m, n) -> int:
        add, count = img[i][j], 1
        if i > 0:
            add += img[i - 1][j]
            count += 1
        if i > 0 and j > 0:
            add += img[i - 1][j - 1]
            count += 1
        if i > 0 and j < n - 1:
            add += img[i - 1][j + 1]
            count += 1
        if j > 0:
            add += img[i][j - 1]
            count += 1
        if j < n - 1:
            add += img[i][j + 1]
            count += 1
        if i < m - 1:
            add += img[i + 1][j]
            count += 1
        if i < m - 1 and j > 0:
            add += img[i + 1][j - 1]
            count += 1
        if i < m - 1 and j < n - 1:
            add += img[i + 1][j + 1]
            count += 1
        return math.floor(add / count)
