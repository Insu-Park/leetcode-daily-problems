class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        splits = []
        i = 0
        splits.append(s[:spaces[0]])
        while i < len(spaces) - 1:
            splits.append(s[spaces[i]:spaces[i + 1]])
            i += 1
        splits.append(s[spaces[-1]:])
        
        return " ".join(splits)
