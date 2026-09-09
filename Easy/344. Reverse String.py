class Solution(object):
    def reverseString(self, s):
        l=len(s)-1
        for i in range(len(s)/2):
            s[i],s[l-i]=s[l-i],s[i]
        return s

# Notes:
# - Use a Two-Pointer approach (or mathematically mirroring indices) to swap characters in-place.
# - Loop up to half the length of the string.
# - Swap the element at index `i` with the element at the corresponding index from the end `len(s) - 1 - i`.
#
# Example Walkthrough: s=['h','e','l','l','o']
# l = 4. loop up to 5/2 = 2 (i=0, 1)
# i=0: swap s[0]('h') and s[4]('o') -> ['o','e','l','l','h']
# i=1: swap s[1]('e') and s[3]('l') -> ['o','l','l','e','h']
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Two Pointers
# Pattern         : In-place Reversal
        
