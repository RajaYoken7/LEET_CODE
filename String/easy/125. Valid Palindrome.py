class Solution(object):
    def isPalindrome(self, s):
        import re
        s=re.sub("[^a-zA-Z0-9]","",s).lower()
        if s==s[::-1]:
            return True
        return False
