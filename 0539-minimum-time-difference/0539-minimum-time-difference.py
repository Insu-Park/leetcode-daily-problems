class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        convert_minutes = []
        for timePoint in timePoints:
            split = timePoint.split(":")
            convert_minutes.append(int(split[0]) * 60 + int(split[1]))
        
        convert_minutes = sorted(convert_minutes)
        n = len(convert_minutes)
        min_time = convert_minutes[0] + (24 * 60 - convert_minutes[n - 1])
        for i in range(1, n):
            diff = convert_minutes[i] - convert_minutes[i - 1]
            min_time = min(min_time, diff)

        return min_time