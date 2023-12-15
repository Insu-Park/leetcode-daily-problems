class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = [i[0] for i in paths]
        for i in paths:
            if i[1] not in start:
                return i[1]