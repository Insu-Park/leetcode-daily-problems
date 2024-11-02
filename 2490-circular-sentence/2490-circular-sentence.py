class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[-1] != sentence[0]:
            return False
        
        words = sentence.split()
        for idx in range(len(words) - 1):
            if words[idx][-1] != words[idx + 1][0]:
                return False
        else:
            return True