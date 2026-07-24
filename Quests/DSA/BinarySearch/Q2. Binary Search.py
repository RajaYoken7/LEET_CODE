class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

# Notes:
# - Standard Binary Search template.
# - Use two pointers `left` and `right` to bound the search space.
# - Calculate `mid`. If `nums[mid]` is the target, return `mid`.
# - If target is larger, search right half (`left = mid + 1`). If smaller, search left half.
#
# Example Walkthrough: nums=[-1,0,3,5,9,12], target=9
# l=0, r=5. mid=2 (3). 3 < 9. l=3.
# l=3, r=5. mid=4 (9). 9 == 9. return 4.
#
# Time Complexity : O(log N)
# Space Complexity: O(1)
# Technique       : Binary Search
# Pattern         : Basic Binary Search