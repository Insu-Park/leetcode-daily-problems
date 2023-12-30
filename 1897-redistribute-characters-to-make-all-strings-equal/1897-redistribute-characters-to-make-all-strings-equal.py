class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counters = {}
        for word in words:
            counters = dict(Counter(counters) + Counter(word))
        
        for item in counters.values():
            if item % len(words) != 0:
                return False

        return True