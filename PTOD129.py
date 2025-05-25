class Solution:
    def pythagoreanTriplet(self, arr):
        num_set = set(arr)
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                c_squared = a * a + b * b
                c = int(c_squared ** 0.5)
                if c * c == c_squared and c in num_set:
                    return True
        return False
