class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        candidates = sorted([c for c in candidates if c <= target])
        n = len(candidates)

        if sum(candidates) < target:
            return []

        def dfs(target, picked, i):
            nonlocal answer
            s = sum(picked)
            if s == target:
                answer.add(tuple(picked))
                return

            for idx in range(i + 1, n):
                if s + candidates[idx] <= target:
                    dfs(target, picked + [candidates[idx]], idx)
                else:
                    break
        
        dfs(target, [], -1)
        
        return answer




        