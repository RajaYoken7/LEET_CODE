class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l


# Notes:
# - Use Binary Search to find the target element's position in O(log N) time.
# - Initialize left (l) and right (r) pointers to the boundaries of the array.
# - In each step, calculate the middle index (mid) and compare nums[mid] with target:
#    - If nums[mid] < target, search the right half (l = mid + 1).
#    - If nums[mid] > target, search the left half (r = mid - 1).
#    - If nums[mid] == target, return mid immediately.
# - If the loop finishes without finding the target, 'l' will point to the correct insertion position.
#
# Example Walkthrough: nums=[1,3,5,6], target=2
# Initial: l=0, r=3
# Iteration 1: mid=1, nums[1]=3. 3 > 2 -> r = 1 - 1 = 0
# Iteration 2: mid=0, nums[0]=1. 1 < 2 -> l = 0 + 1 = 1
# Loop ends (l > r). Return l (which is 1).
#
# Time Complexity : O(log N)
# Space Complexity: O(1)
# Technique       : Binary Search
# Pattern         : Search Insert Position / Sorted Array