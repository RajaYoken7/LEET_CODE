class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 1. Double the string: s + s
        # 2. Remove the very first and very last characters
        # 3. Check if the original s exists in the remaining string
        return s in (s + s)[1:-1]