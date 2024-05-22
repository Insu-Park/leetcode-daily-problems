class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        answer = []

        def dfs(start, l):
            if start == n:
                answer.extend([l])
            else:
                for end in range(start + 1, n + 1):
                    if s[start:end] == s[start:end][::-1]:
                        new_list = copy.deepcopy(l)
                        new_list.append(s[start:end])
                        dfs(end, new_list)

        dfs(0, [])
        return answer