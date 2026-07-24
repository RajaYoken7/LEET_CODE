class Solution(object):
    def threeSum(self, nums):
        new_arr = []
        nums.sort()  # Sort to make skipping duplicates easy
        
        for i in range(len(nums) - 2):
           
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == 0:
                    new_arr.append([nums[i], nums[left], nums[right]])
                    
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return new_arr

# Notes:
# - Sort the array first to use the Two-Pointer approach and easily skip duplicates.
# - Iterate through the array with `i` as the first element.
# - Use `left` and `right` pointers to find the other two elements that sum to `-nums[i]`.
# - Skip duplicate values for `i`, `left`, and `right` to avoid duplicate triplets.
#
# Example Walkthrough: nums=[-1,-1,2] (sorted)
# i=0 (-1). left=1 (-1), right=2 (2). sum = -1 -1 + 2 = 0.
# Add to result. Skip duplicates.
#
# Time Complexity : O(N^2)
# Space Complexity: O(1) or O(N) for sorting
# Technique       : Two Pointers
# Pattern         : Target Sum / K-Sum
