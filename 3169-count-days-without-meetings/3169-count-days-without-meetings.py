class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0])
        free_days = max(meetings[0][0] - 1, 0)
        merged_interval = meetings[0]

        for i in range(1, len(meetings)):
            if meetings[i][0] > merged_interval[1]:
                free_days += max(meetings[i][0] - merged_interval[1] - 1, 0)
                merged_interval = meetings[i]
            else:
                merged_interval = [merged_interval[0], max(meetings[i][1], merged_interval[1])]

        free_days += max(days - merged_interval[1], 0)
        return free_days