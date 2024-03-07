class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = set()
        start, now, answer = 0, 0, 0
        while now < len(s):
            if s[now] in subs:
                while s[start] != s[now]:
                    start += 1
                start += 1
                subs = set(s[start:now])

            subs.add(s[now])
            answer = max(answer, len(subs))
            now += 1
            
        return answer