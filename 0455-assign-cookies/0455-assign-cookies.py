class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer, s_index, g_index = 0, 0, 0
        g.sort()
        s.sort()
        while s_index < len(s) and g_index < len(g):
            if g[g_index] <= s[s_index]:
                answer += 1
                s_index += 1
                g_index += 1
            else:
                s_index += 1

        return answer