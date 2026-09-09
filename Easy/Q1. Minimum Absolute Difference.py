class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        min_diff = float('inf')

        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])

        ans = []

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i + 1]])

        return ans

# Notes:
# - Sort the array first so the minimum difference can only be between adjacent elements.
# - First pass: Find the absolute minimum difference by checking all adjacent pairs.
# - Second pass: Collect all pairs that have exactly this minimum difference.
# - Sorting simplifies the problem from comparing every pair to just adjacent ones.
#
# Example Walkthrough: arr=[4,2,1,3] -> sorted: [1,2,3,4]
# Pass 1: Min diff between (1,2), (2,3), (3,4) is 1.
# Pass 2: Collect pairs with diff=1 -> [[1,2], [2,3], [3,4]].
#
# Time Complexity : O(N log N)
# Space Complexity: O(1) or O(N) depending on sorting
# Technique       : Sorting
# Pattern         : Adjacent Elements Comparison