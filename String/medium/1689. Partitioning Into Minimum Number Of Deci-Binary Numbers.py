class Solution:
    def minPartitions(self, n: str) -> int:
        return ord(max(x for x in n))-ord('0')

# Notes:
# - A deci-binary number only consists of 0s and 1s.
# - To form a number `n` by adding deci-binary numbers, the minimum number of such numbers required is exactly equal to the maximum digit in `n`.
# - If the max digit is 9, we need at least 9 deci-binary numbers because each can only contribute at most 1 to that digit position.
#
# Example Walkthrough: n="32"
# Max digit is '3'. We need 3 numbers.
# e.g., 11 + 11 + 10 = 32.
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Math / Observation
# Pattern         : String Parsing
