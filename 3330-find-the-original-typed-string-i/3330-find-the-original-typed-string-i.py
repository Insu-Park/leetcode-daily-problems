class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        count = 1
        last = word[0]

        for i in range(1, len(word)):
            if word[i] != last:
                answer += count - 1
                count = 1
                last = word[i]
            else:
                count += 1

        answer += count - 1
        return answer