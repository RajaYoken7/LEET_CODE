import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 1. Calculate the minimum number of repetitions to match b's length
        # min_repeat = ceil(len(b) / len(a))
        min_repeat = math.ceil(len(b) / len(a))
        
        # 2. Check if b is in a repeated min_repeat times
        if b in (a * min_repeat):
            return min_repeat
        
        # 3. Check if b is in a repeated min_repeat + 1 times
        # This handles cases where b starts at the end of a and wraps around
        if b in (a * (min_repeat + 1)):
            return min_repeat + 1
            
        # 4. If neither works, it's impossible
        return -1

# Notes:
# - Calculate the minimum number of times `a` must be repeated to at least cover the length of `b`. Let this be `min_repeat`.
# - `b` can either be fully contained within `a * min_repeat`.
# - Or, `b` might start near the end of the first `a` and spill over into an extra repetition: `a * (min_repeat + 1)`.
# - If it's in neither, it's impossible to form `b`.
#
# Example Walkthrough: a="abcd", b="cdabcdab"
# len(a)=4, len(b)=8. min_repeat = ceil(8/4) = 2.
# a*2 = "abcdabcd". b not in a*2.
# a*3 = "abcdabcdabcd". b IS in a*3 ("ab[cdabcdab]cd").
# Return 3.
#
# Time Complexity : O(N * (N + M)) for substring search
# Space Complexity: O(N + M) for string concatenation
# Technique       : String Concatenation / Math
# Pattern         : Substring Search