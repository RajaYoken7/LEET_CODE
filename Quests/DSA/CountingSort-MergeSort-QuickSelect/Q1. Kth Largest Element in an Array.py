class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]

# Notes:
# - Brute-force approach using sorting.
# - Sort the array in ascending order, then return the `k`-th element from the end (`-k`).
# - More optimal approaches include using a Min-Heap of size K or QuickSelect.
#
# Example Walkthrough: nums=[3,2,1,5,6,4], k=2
# sort -> [1,2,3,4,5,6]
# return nums[-2] -> 5
#
# Time Complexity : O(N log N)
# Space Complexity: O(1) or O(N) depending on sort
# Technique       : Sorting
# Pattern         : Kth Element