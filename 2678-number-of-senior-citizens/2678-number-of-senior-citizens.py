class Solution:
    def countSeniors(self, details: List[str]) -> int:
        answer = 0
        for detail in details:
            if detail[11:13] > "60":
                answer += 1
        return answer