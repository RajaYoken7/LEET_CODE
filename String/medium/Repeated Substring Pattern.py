class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 1. Double the string: s + s
        # 2. Remove the very first and very last characters
        # 3. Check if the original s exists in the remaining string
        return s in (s + s)[1:-1]

# Notes:
# - If a string `s` is made of a repeated substring `P` (e.g., `s = P + P`), then doubling it gives `s + s = P + P + P + P`.
# - Removing the first and last characters destroys the first and last `P`.
# - The remaining string `(s + s)[1:-1]` will still contain `P + P` (which is `s`) IF AND ONLY IF `s` is a repeated substring.
#
# Example Walkthrough: s="abab"
# s+s = "abababab"
# Strip ends: "bababa"
# Does "abab" exist in "bababa"? Yes. Return True.
#
# Time Complexity : O(N) for substring search (using optimized algorithms)
# Space Complexity: O(N) for creating the doubled string
# Technique       : String Manipulation
# Pattern         : Substring Search