class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        answer = []
        d = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        teens = {
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        def process(num):
            s = []
            if num >= 100:
                s.append(d[num // 100])
                s.append("Hundred")
                num %= 100
            if num in teens:
                s.append(teens[num])
            else:
                if num >= 10:
                    s.append(d[num - (num % 10)])
                s.append(d[num % 10])
            return s

        if num >= 10 ** 9:
            q = num // 10 ** 9
            answer.append(d[q])
            answer.append("Billion")
            num %= 10 ** 9
        
        if num >= 10 ** 6:
            q = num // 10 ** 6
            answer.extend(process(q))
            answer.append("Million")
            num %= 10 ** 6
            
        if num >= 10 ** 3:
            q = num // 10 ** 3
            answer.extend(process(q))
            answer.append("Thousand")
            num %= 10 ** 3

        answer.extend(process(num))
        print(answer)

        return " ".join(answer)