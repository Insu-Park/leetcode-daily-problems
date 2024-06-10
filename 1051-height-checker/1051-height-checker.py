class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        answer = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                answer += 1
        return answer