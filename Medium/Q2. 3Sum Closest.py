class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array to use the two-pointer technique
        nums.sort()
        n = len(nums)
        # Initialize closest_sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # xrange is preferred over range in Python 2 for memory efficiency
        xrange = None
        for i in xrange(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find the exact target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

# Notes:
# - Sort the array to use the Two-Pointer technique.
# - Iterate through with `i` as the first element, and use `left` and `right` pointers for the remaining array.
# - Calculate the `current_sum`. If it exactly matches `target`, return it early.
# - Track the `closest_sum` by comparing absolute differences.
# - Adjust pointers: if sum < target, move `left` rightward to increase sum; else move `right` leftward.
#
# Example Walkthrough: nums=[-1,2,1,-4], target=1
# sort: [-4,-1,1,2]. closest = -4-1+1 = -4.
# i=0 (-4): l=1 (-1), r=3 (2). sum = -3. abs(-3 - 1)=4 < abs(-4 - 1)=5. closest=-3. sum < 1 -> l=2 (1).
# sum = -4+1+2 = -1. abs(-1 - 1)=2 < 4. closest=-1.
#
# Time Complexity : O(N^2)
# Space Complexity: O(1) or O(N) for sorting
# Technique       : Two Pointers
# Pattern         : Target Sum / K-Sum
