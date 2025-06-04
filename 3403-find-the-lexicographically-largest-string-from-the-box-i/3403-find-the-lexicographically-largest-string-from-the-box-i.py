class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        l = len(word) - numFriends + 1
        answer = word[0]
        for i in range(len(word) - l + 1):
            answer = max(word[i:i + l], answer)

        for i in range(1, l):
            answer = max(word[-i:], answer)

        return answer 