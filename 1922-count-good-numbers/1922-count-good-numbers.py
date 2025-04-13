class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        def modular_exponentiation(a, b, m):
            result = 1
            a = a % m
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % m
                a = (a * a) % m
                b //= 2
            return result
        
        p, q = (n + 1) // 2, n // 2
        return modular_exponentiation(5, p, MOD) * modular_exponentiation(4, q, MOD) % MOD
        