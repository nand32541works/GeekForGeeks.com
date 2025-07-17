class Solution:
    def primeFactors(self, num):
        factors = []
        count = 0
        while num % 2 == 0:
            num //= 2
            count += 1
        if count > 0:
            factors.append([2, count])
        i = 3
        while i * i <= num:
            count = 0
            while num % i == 0:
                num //= i
                count += 1
            if count > 0:
                factors.append([i, count])
            i += 2
        if num > 1:
            factors.append([num, 1])
        return factors
    def legendre(self, n, p):
        count = 0
        power = p
        while power <= n:
            count += n // power
            power *= p
        return count
    def maxKPower(self, n, k):
        factors = self.primeFactors(k)
        result = float('inf')
        for prime, expInK in factors:
            countInFact = self.legendre(n, prime)
            result = min(result, countInFact // expInK)
        return result
