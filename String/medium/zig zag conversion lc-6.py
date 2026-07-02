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
            
            
        
