class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = Counter(s1.split() + s2.split())
        return [k for k, v in s.items() if v == 1]