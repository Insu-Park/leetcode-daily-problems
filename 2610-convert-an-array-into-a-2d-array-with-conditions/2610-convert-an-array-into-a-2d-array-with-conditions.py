class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer, dics = [], [{}]
        for num in nums:
            for dic in dics:
                if num not in dic:
                    dic[num] = 1
                    break
            else:
                dics.append({num: 1})
        
        for dic in dics:
            answer.append(dic.keys())

        return answer