class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        nums = [True] * (10 ** 6 + 1)
        last_prime = -1
        answer = [-1, -1]
        diff = 10 ** 6
        for i in range(2, right + 1):
            if nums[i] == True:
                for j in range(i * 2, right + 1, i):
                    nums[j] = False
        
        for i in range(max(left, 2), right + 1):
            if nums[i] == True:
                if last_prime == -1:
                    last_prime = i
                else:
                    if i - last_prime < diff:
                        answer = [last_prime, i]
                        diff = i - last_prime
                    last_prime = i

        return answer

