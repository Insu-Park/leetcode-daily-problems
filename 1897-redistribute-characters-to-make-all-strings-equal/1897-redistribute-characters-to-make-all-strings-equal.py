class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        word = "".join(words)
        for it in Counter(word).values():
            if it % len(words) != 0:
                return False

        return True