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