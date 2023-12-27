class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        start = 0
        end = 1
        for index, color in enumerate(colors[:-1]):
            if color == colors[index + 1]:
                end = index + 2
            else:
                answer += sum(neededTime[start:end]) - max(neededTime[start:end]) 
                start, end = index + 1, index + 2
        
        answer += sum(neededTime[start:end]) - max(neededTime[start:end]) 
        return answer