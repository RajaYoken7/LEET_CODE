class Solution(object):
    def magicalString(self, n):
        if n<=3:
            return 1
        else:
            s="122"
            i=len(s)-1
            while True:
                if s[-1]=='2':
                    s=s+('1'*int(s[i]))

                else:
                    s=s+('2'*int(s[i]))
                if len(s)>=n:
                    break
                i=i+1
            s=s[:n]
            return s.count('1')
        
# Notes:
# 1. The magical string starts with "122".
# 2. Pointer 'i' reads the current group length (1 or 2).
# 3. The last character of the string decides what to append next:
#    - Last = '2' -> Append '1'
#    - Last = '1' -> Append '2'
# 4. Append the next character 'int(s[i])' times.
# 5. Increment 'i' to read the next group length.
# 6. Continue until the string length reaches at least n.
# 7. Count the number of '1's in the first n characters.

# Example:
# Start: 122
# i = 2, s[i] = '2', last = '2' -> Append "11" -> 12211
# i = 3, s[i] = '1', last = '1' -> Append "2"  -> 122112
# i = 4, s[i] = '1', last = '2' -> Append "1"  -> 1221121
# ...

# Time Complexity : O(n)
# Space Complexity: O(n)
# Technique        : Simulation / String Generation
