class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer, rows = [], [set()]
        for num in nums:
            for row in rows:
                if num not in row:
                    row.add(num)
                    break
            else:
                rows.append(set([num]))
        
        for row in rows:
            answer.append(list(row))

        return answer