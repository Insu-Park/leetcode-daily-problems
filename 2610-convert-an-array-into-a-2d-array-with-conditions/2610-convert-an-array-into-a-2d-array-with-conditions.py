class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rows = []
        for num in nums:
            for row in rows:
                if num not in row:
                    row.add(num)
                    break
            else:
                rows.append(set([num]))
        

        return rows