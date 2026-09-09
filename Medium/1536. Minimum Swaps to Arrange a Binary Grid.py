from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = list(map(lambda r: (r[::-1] + [1]).index(1), grid))
        
        swaps = 0
        for i in range(n):
            j = (zeros + [n]).index(next(filter(lambda v: v >= n - 1 - i, zeros + [n])))
            if j == len(zeros): return -1
            swaps += j
            zeros.pop(j)
        return swaps

# Notes:
# - Convert each row to a single number representing the count of trailing zeros.
# - For row `i`, we need at least `n - 1 - i` trailing zeros.
# - Find the first row from the current position downwards that satisfies this condition.
# - "Swap" it up to row `i` by tracking the number of steps (swaps) it took and removing it from the list.
#
# Example Walkthrough: n=3, zeros=[0,2,1]
# i=0 (needs 2 zeros). Found at index 1. Swaps += 1. zeros becomes [0, 1].
# i=1 (needs 1 zero). Found at index 1. Swaps += 1. zeros becomes [0].
# Total swaps = 2.
#
# Time Complexity : O(N^2)
# Space Complexity: O(N)
# Technique       : Greedy / Array Manipulation
# Pattern         : Minimum Swaps
