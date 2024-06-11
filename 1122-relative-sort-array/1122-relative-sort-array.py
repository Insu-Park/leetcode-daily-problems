class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        answer = []
        for item in arr2:
            n = c[item]
            for it in range(n):
                answer.append(item)
            del c[item]
        
        s = sorted(c.items())
        for key, value in s:
            for it in range(value):
                answer.append(key)
        
        return answer