class Solution:
    def fractionAddition(self, expression: str) -> str:
        answer = 0
        operators = []
        nums = []

        if expression[0] != "-":
            expression = "+" + expression

        for i in range(len(expression)):
            if expression[i] == '-' or expression[i] == '+':
                operators.append((expression[i], i))
                
        for i in range(1, len(operators)):
            num = expression[operators[i - 1][1] + 1:operators[i][1]]
            nums.append(list(map(int, num.split("/"))))

        nums.append(list(map(int, expression[operators[-1][1] + 1:].split("/"))))
        lcm = 1
        for _, d in nums:
            lcm = math.lcm(lcm, d)

        for i, (n, d) in enumerate(nums):
            tmp = n * (lcm // d)
            answer = answer + tmp if operators[i][0] == "+" else answer - tmp

        gcd = math.gcd(answer, lcm)
        n, d = answer // gcd, lcm // gcd
        return str(n) + "/" + str(d)



