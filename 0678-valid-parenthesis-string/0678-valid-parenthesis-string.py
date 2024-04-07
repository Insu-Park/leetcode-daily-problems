class Solution:
    def checkValidString(self, s: str) -> bool:
        idx, left, right, star = 0, 0, 0, 0
        while idx < len(s):
            if s[idx] == '(': left += 1
            elif s[idx] == ')': right += 1
            elif s[idx] == '*': star += 1
            if right > left + star:
                return False
            idx += 1

        if left > right + star:
            return False
        return True
        