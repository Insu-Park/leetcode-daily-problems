class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        l = len(searchWord)
        for idx, word in enumerate(words, 1):
            if len(word) >= l and word[:l] == searchWord:
                return idx
        else:
            return -1