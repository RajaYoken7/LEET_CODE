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