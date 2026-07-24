class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

# Notes:
# - Use a two-pointer approach where `j` keeps track of the next position to place a non-zero element.
# - Iterate `i` through the array. Whenever a non-zero is found, swap it with the element at `j`.
# - Increment `j` after swapping to prepare for the next non-zero.
#
# Example Walkthrough: nums=[0,1,0,3]
# i=0 (0): ignore. j=0
# i=1 (1): swap nums[1] & nums[0] -> [1,0,0,3]. j=1
# i=2 (0): ignore. j=1
# i=3 (3): swap nums[3] & nums[1] -> [1,3,0,0]. j=2
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Two Pointers
# Pattern         : In-place Array Partitioning
