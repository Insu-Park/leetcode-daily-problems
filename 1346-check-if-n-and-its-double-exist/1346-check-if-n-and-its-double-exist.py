class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = Counter(arr)
        if d[0] > 1:
            return True

        for a in arr:
            if a != 0 and 2 * a in d.keys():
                return True
        else:
            return False