class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_dict = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        tmp_list = []
        for ch in s:
            if ch in vowels_dict:
                tmp_list.append(ch)

        tmp_list = sorted(tmp_list, reverse=True)
        s = list(s)
        for index, ch in enumerate(s):
            if ch in vowels_dict:
                s[index] = tmp_list.pop()

        return "".join(s)