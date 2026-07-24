class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 1. Rotations only work if the lengths are identical
        if len(s) != len(goal):
            return False
            
        # 2. If goal is a rotation of s, it must exist within s + s
        return goal in (s + s)

# Notes:
# - A string `goal` is a rotation of `s` if it is a substring of `s + s` and has the exact same length.
# - Concatenating `s` with itself (`s + s`) covers all possible rotations of `s`.
# - For example, if s="abcde", rotations are "bcdea", "cdeab", etc., which are all in "abcdeabcde".
#
# Example Walkthrough: s="abcde", goal="cdeab"
# s + s = "abcdeabcde"
# "cdeab" is in "ab[cdeab]cde". Returns True.
#
# Time Complexity : O(N^2) due to substring search, but typically very fast in Python
# Space Complexity: O(N) for creating `s + s`
# Technique       : String Concatenation
# Pattern         : Substring Search