class Solution(object):
    def getMinDistance(self, nums, target, start):
        ans = float('inf')  
        
        for i in range(len(nums)):
            if nums[i] == target:
                a = abs(i - start)
                if a < ans:
                    ans = a
                    
        return ans

# Notes:
# - Simple linear scan to find all occurrences of the target element.
# - For each target found, calculate its absolute distance from the `start` index.
# - Update the minimum distance (`ans`) if the current distance is smaller.
#
# Example Walkthrough: nums=[1,2,3,4,5], target=5, start=3
# Target 5 found at i=4.
# Distance = abs(4 - 3) = 1. ans updated to 1.
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Linear Scan
# Pattern         : Array Traversal
