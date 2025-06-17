class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        maxN = n
        fact = [1] * (maxN)
        inv_fact = [1] * (maxN)
        for i in range(1, maxN):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[maxN - 1] = pow(fact[maxN - 1], MOD - 2, MOD)
        for i in range(maxN - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
        res = comb(n - 1, k) * m % MOD
        res = res * pow(m - 1, n - 1 - k, MOD) % MOD
        return res