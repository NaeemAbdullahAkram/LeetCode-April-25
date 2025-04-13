class Solution:
    M = 10**9 + 7  # Modulo value to keep the number within bounds
    def countGoodNumbers(self, n: int) -> int:
        # Fast exponentiation (binary exponentiation)
        def findPower(a, b):
            if b == 0:
                return 1
            half = findPower(a, b // 2) % self.M
            result = (half * half) % self.M
            if b % 2:
                result = (result * a) % self.M
            return result

        # Total count = 5^(ceil(n/2)) * 4^(floor(n/2)) % (10^9 + 7)
        even_count = (n + 1) // 2  # Number of even-indexed digits
        odd_count = n // 2         # Number of odd-indexed digits

        return (findPower(5, even_count) * findPower(4, odd_count)) % self.M