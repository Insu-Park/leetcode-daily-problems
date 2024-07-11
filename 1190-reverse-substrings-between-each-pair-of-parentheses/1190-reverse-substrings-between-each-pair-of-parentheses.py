class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s = list(s)
        idx = 0
        while idx < len(s):
            if s[idx] == "(":
                stack.append(idx)
                s.pop(idx)
            elif s[idx] == ")":
                s.pop(idx)
                start = stack.pop()

                print(s[start:idx], start, idx)
                s[start:idx] = s[start:idx][::-1]
                print(s)
            else:
                idx += 1

        return "".join(s)
