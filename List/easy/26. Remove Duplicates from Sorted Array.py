class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        k = 1  # position for next unique element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

# Notes:
# - Use a two-pointer approach where `k` tracks the position for the next unique element.
# - Iterate through the array starting from the second element (i=1).
# - When a new unique element is found (nums[i] != nums[k-1]), place it at index `k` and increment `k`.
# - Because the array is sorted, duplicates are always adjacent.
#
# Example Walkthrough: nums=[1,1,2]
# k=1. i=1: nums[1]==nums[0], skip.
# i=2: nums[2]!=nums[0] (2!=1). nums[1] = 2. k=2.
# Result: k=2, nums=[1,2,...]
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Two Pointers
# Pattern         : In-place Array Modification
