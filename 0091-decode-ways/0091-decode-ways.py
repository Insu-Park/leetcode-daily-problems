class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        answer_list = [0] * (len(s) + 1)
        answer_list[0] = 1
        answer_list[1] = 1

        for index in range(2, len(s) + 1):
            if s[index - 1] != "0":
                answer_list[index] += answer_list[index - 1]
            if "10" <= s[index - 2:index] <= "26":
                answer_list[index] += answer_list[index - 2]

        return answer_list[-1]