class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float('-inf')

        for ch_a in '01234':
            for ch_b in '01234':
                if ch_a == ch_b:
                    continue

                cnt_a = [0] * (n + 1)
                cnt_b = [0] * (n + 1)

                for i in range(n):
                    cnt_a[i + 1] = cnt_a[i] + (s[i] == ch_a)
                    cnt_b[i + 1] = cnt_b[i] + (s[i] == ch_b)

                best_diff = [[float('-inf')] * 2 for _ in range(2)]
                l = 1

                for r in range(k, n + 1):
                    while r - l + 1 >= k and cnt_a[r] > cnt_a[l - 1] and cnt_b[r] > cnt_b[l - 1]:
                        pa = cnt_a[l - 1] % 2
                        pb = cnt_b[l - 1] % 2
                        best_diff[pa][pb] = max(best_diff[pa][pb], cnt_b[l - 1] - cnt_a[l - 1])
                        l += 1

                    pa = cnt_a[r] % 2
                    pb = cnt_b[r] % 2
                    diff = best_diff[pa ^ 1][pb]
                    if diff != float('-inf'):
                        ans = max(ans, cnt_a[r] - cnt_b[r] + diff)

        return -1 if ans == float('-inf') else ans