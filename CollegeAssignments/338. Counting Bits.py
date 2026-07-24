class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            binary = bin(i)
            ans.append(binary.count('1')) 
        return ans

# Notes:
# - Iterate from 0 to n and use Python's built-in `bin()` to get the binary string.
# - Count the number of '1's in the string representation.
# - Append the count to the result list.
# - This is a straightforward simulation approach.
#
# Example Walkthrough: n=2
# i=0: bin(0)='0b0', count('1')=0. ans=[0]
# i=1: bin(1)='0b1', count('1')=1. ans=[0,1]
# i=2: bin(2)='0b10', count('1')=1. ans=[0,1,1]
#
# Time Complexity : O(N * log(N)) since counting bits takes O(log i)
# Space Complexity: O(1) excluding output array
# Technique       : Simulation / Built-in Functions
# Pattern         : Bit Manipulation