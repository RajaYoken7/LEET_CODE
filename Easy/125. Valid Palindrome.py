class Solution(object):
    def isPalindrome(self, s):
        import re
        s=re.sub("[^a-zA-Z0-9]","",s).lower()
        if s==s[::-1]:
            return True
        return False

# Notes:
# - Clean the string by removing all non-alphanumeric characters using a regular expression and convert to lowercase.
# - Check if the cleaned string is equal to its reverse (`s[::-1]`).
# - This is a Pythonic, concise approach, although two pointers would avoid creating new strings.
#
# Example Walkthrough: s="A man, a plan, a canal: Panama"
# Cleaned: "amanaplanacanalpanama"
# Reversed: "amanaplanacanalpanama". Equal -> True.
#
# Time Complexity : O(N)
# Space Complexity: O(N) for creating new strings
# Technique       : String Manipulation / Regex
# Pattern         : Palindrome Check
