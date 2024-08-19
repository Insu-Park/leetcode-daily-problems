class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 2

        answer = 0
        i = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        while i < len(primes):
            if n % primes[i] != 0:
                i += 1
            else:
                n = n // primes[i]
                answer += primes[i]
                if n == 1:
                    return answer