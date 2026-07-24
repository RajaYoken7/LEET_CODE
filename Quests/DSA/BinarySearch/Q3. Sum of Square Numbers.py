class Solution(object):
    def judgeSquareSum(self, c):
        divisor = 2
        while divisor * divisor <= c:
            if c % divisor == 0:
                exponentCount = 0
                while c % divisor == 0:
                    exponentCount += 1
                    c //= divisor
                if divisor % 4 == 3 and exponentCount % 2 != 0:
                    return False
            divisor += 1
        return c % 4 != 3

# Notes:
# - Use prime factorization properties (Fermat's Theorem on sums of two squares).
# - A number can be expressed as the sum of two squares if and only if every prime factor of the form `4k + 3` occurs an even number of times.
# - Iterate through possible prime divisors up to `sqrt(c)`.
#
# Example Walkthrough: c=5
# div=2: 5%2!=0.
# div=3: 9 <= 5 is false. Loop ends.
# return 5 % 4 != 3 -> True.
#
# Time Complexity : O(sqrt(C))
# Space Complexity: O(1)
# Technique       : Math / Prime Factorization
# Pattern         : Sum of Squares