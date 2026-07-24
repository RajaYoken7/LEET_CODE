class Solution:
    def maskPII(self, s: str) -> str:
        # 1. Identify type: Email contains '@'
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            # Mask email: first char + 5 asterisks + last char + @ + domain
            return f"{name[0]}*****{name[-1]}@{domain}"
        
        # 2. Identify type: Phone Number
        else:
            # Strip all non-digit characters
            digits = "".join(c for c in s if c.isdigit())
            local = "***-***-" + digits[-4:]
            
            # Determine country code based on total digit count
            country_codes = {
                10: "",
                11: "+*-",
                12: "+**-",
                13: "+***-"
            }
            
            return country_codes[len(digits)] + local

# Notes:
# - Separate logic for Email and Phone Number based on the presence of `@`.
# - For emails, extract the first and last character of the local name, convert to lowercase, and format with `*****`.
# - For phone numbers, strip all non-digit characters, extract the last 4 digits, and determine the country code mask based on total digits.
#
# Example Walkthrough: s="LeetCode@LeetCode.com"
# Email: name="leetcode", domain="leetcode.com"
# Mask: l*****e@leetcode.com
#
# Time Complexity : O(N)
# Space Complexity: O(N) for string manipulation
# Technique       : String Parsing / Conditional Logic
# Pattern         : String Formatting