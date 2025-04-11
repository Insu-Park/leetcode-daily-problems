class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for i in range(low, high + 1):
            if (i >= 1000 or i <= 100) and ((i // 10 == i % 10) or (sum(map(int,str(i % 100))) == sum(map(int,str(i // 100))))):
                print(i)
                answer += 1

        return answer
            
        
        