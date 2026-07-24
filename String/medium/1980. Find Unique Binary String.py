from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('1' if x[i]=='0' else '0' for i, x in enumerate(nums))

# Notes:
# - Use Cantor's Diagonalization argument.
# - Construct a new binary string by flipping the `i`-th character of the `i`-th string in the given list.
# - This guarantees the new string differs from the 1st string at index 0, the 2nd string at index 1, etc., making it unique.
#
# Example Walkthrough: nums=["01", "10"]
# i=0, x="01": x[0]='0' -> '1'.
# i=1, x="10": x[1]='0' -> '1'.
# Result: "11", which is not in the list.
#
# Time Complexity : O(N)
# Space Complexity: O(N) for storing the new string
# Technique       : Cantor's Diagonalization
# Pattern         : String Construction
