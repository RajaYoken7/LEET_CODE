class Solution(object):
    def findComplement(self, num):
        return num ^ ((1 << num.bit_length()) - 1)

# Notes:
# - The complement is found by flipping all the bits of the number.
# - We can achieve this by XORing the number with a bitmask of all 1s of the same length.
# - `num.bit_length()` gives the number of bits. `(1 << length) - 1` creates the mask of 1s.
# - E.g., for 5 (101), length is 3. Mask is (1 << 3) - 1 = 8 - 1 = 7 (111).
# - 5 ^ 7 = 101 ^ 111 = 010 (2).
#
# Example Walkthrough: num=5 (101 in binary)
# bit_length = 3. Mask = (1 << 3) - 1 = 7 (111 in binary).
# 5 ^ 7 = 2 (010).
#
# Time Complexity : O(1)
# Space Complexity: O(1)
# Technique       : Bitmask / XOR
# Pattern         : Bit Manipulation