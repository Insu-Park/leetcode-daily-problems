class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr_set = [set()]
        for s in arr:
            if len(set(s)) != len(s):
                continue
            s = set(s)
            for item in arr_set:
                if s & item:
                    continue
                arr_set.append(item | s)
 
        return max([len(item) for item in arr_set])
        
