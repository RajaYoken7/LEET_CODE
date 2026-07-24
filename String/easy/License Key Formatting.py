class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 1. Remove existing dashes and convert to uppercase
        clean_s = s.replace("-", "").upper()
        
        # 2. Convert to list for efficient modification
        res = []
        n = len(clean_s)
        
        # 3. Traverse the string backwards
        # We start from the end and take chunks of size k
        for i in range(n, 0, -k):
            # i is the end of the chunk, i-k is the start (clamped to 0)
            start = max(0, i - k)
            res.append(clean_s[start:i])
            
        # 4. Join the chunks with dashes and reverse them back to the correct order
        # We reverse because we appended chunks from the end of the string
        return "-".join(res[::-1])

# Notes:
# - Remove all dashes and convert the string to uppercase to get a clean string.
# - Traverse the clean string backwards taking chunks of size `k`.
# - Use slicing `clean_s[start:i]` to extract each chunk and append it to a result list.
# - Join the result list with dashes and reverse it (since we built it backwards) to get the final formatted key.
#
# Example Walkthrough: s="5F3Z-2e-9-w", k=4
# clean_s = "5F3Z2E9W". len=8.
# i=8: start=4, chunk="2E9W". res=["2E9W"]
# i=4: start=0, chunk="5F3Z". res=["2E9W", "5F3Z"]
# reversed and joined: "5F3Z-2E9W"
#
# Time Complexity : O(N)
# Space Complexity: O(N)
# Technique       : String Manipulation / Slicing
# Pattern         : String Formatting