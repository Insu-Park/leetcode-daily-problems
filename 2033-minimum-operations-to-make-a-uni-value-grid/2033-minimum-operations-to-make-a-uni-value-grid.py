class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        new_list = []
        grid_sum = 0
        remainders = grid[0][0] % x
        for row in grid:
            for item in row:
                if item % x != remainders:
                    return -1
                
                grid_sum += item
                new_list.append(item)

        new_list.sort()
        mid = len(new_list) // 2
        target = new_list[mid]
        answer = 0
        for i in new_list:
            answer += (abs(target - i)) // x

        return answer