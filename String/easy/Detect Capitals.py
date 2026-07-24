class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All letters are capitals (e.g., "USA")
        # Case 2: All letters are lowercase (e.g., "leetcode")
        # Case 3: Only the first letter is capital (e.g., "Google")
        
        return word.isupper() or word.islower() or word.istitle()

# Notes:
# - The problem requires checking if the string matches one of three specific capitalization rules.
# - Python strings have built-in methods that perfectly map to these rules:
#   `isupper()` checks if ALL letters are capital.
#   `islower()` checks if ALL letters are lowercase.
#   `istitle()` checks if ONLY the first letter is capital (and the rest are lowercase).
#
# Example Walkthrough: word="Google"
# isupper() -> False. islower() -> False. istitle() -> True.
# Returns True.
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Built-in String Functions
# Pattern         : String Validation