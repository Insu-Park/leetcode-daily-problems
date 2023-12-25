class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        answer_list = [0] * (len(s) + 1)
        answer_list[0] = 1
        answer_list[1] = 1

        for index in range(2, len(s) + 1):
            one_digit = s[index - 1]
            two_digits = s[index - 2:index]

            if one_digit != "0":
                answer_list[index] += answer_list[index - 1]

            if "10" <= two_digits <= "26":
                answer_list[index] += answer_list[index - 2]

        return answer_list[-1]