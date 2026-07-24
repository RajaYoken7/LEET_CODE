class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""]*numRows
        row = 0
        ascending = True
        for char in s:
            rows[row] += char
            if ascending:
                if row<numRows-1:
                    row += 1
                else:
                    row -= 1
                    ascending = False
            else:
                if row > 0:
                    row -= 1
                else:
                    row += 1
                    ascending = True
        
        result = ""
        for string in rows:
            result += string

        return result

# Notes:
# - Create an array of strings for each row.
# - Iterate through the string `s`, placing each character in the current row.
# - Keep a boolean flag `ascending` (going down) to track the direction.
# - Reverse direction when hitting the top (row 0) or bottom (numRows - 1) row.
# - Join all rows to get the final converted string.
#
# Example Walkthrough: s="PAYPALISHIRING", numRows=3
# rows=["", "", ""]
# 'P' -> row 0. 'A' -> row 1. 'Y' -> row 2. (hit bottom, reverse)
# 'P' -> row 1. 'A' -> row 0. (hit top, reverse)...
# Finally: join rows.
#
# Time Complexity : O(N)
# Space Complexity: O(N) for storing rows
# Technique       : Simulation / Array of Strings
# Pattern         : Matrix Traversal
            
            
        
