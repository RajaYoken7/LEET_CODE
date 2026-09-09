class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_water = width * current_height
            max_water = max(max_water, current_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

# Notes:
# - Use a Two-Pointer approach starting from both ends of the array.
# - The area is determined by the shorter line and the distance between them.
# - To maximize the area, always move the pointer pointing to the shorter line inward.
#
# Example Walkthrough: height=[1,8,6,2,5,4,8,3,7]
# left=0(1), right=8(7). area = min(1,7) * 8 = 8.
# left height is smaller, so move left to 1(8).
# area = min(8,7) * 7 = 49.
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Two Pointers
# Pattern         : Maximize Area
