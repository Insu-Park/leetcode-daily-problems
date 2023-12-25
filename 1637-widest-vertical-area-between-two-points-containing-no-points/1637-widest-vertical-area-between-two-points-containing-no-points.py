class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        x_points = [0] * n
        subs = [0] * (n - 1)

        for index, item in enumerate(points):
            x_points[index] = item[0]

        x_points.sort()
        for index in range(n - 1):
            subs[index] = x_points[index+1] - x_points[index]
        
        return max(subs)
            