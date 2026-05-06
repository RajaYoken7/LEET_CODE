class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All letters are capitals (e.g., "USA")
        # Case 2: All letters are lowercase (e.g., "leetcode")
        # Case 3: Only the first letter is capital (e.g., "Google")
        
        return word.isupper() or word.islower() or word.istitle()