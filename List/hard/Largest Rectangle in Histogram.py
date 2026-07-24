class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1] # Initialize with -1 to handle the left boundary
        max_area = 0
        heights.append(0) # Add a sentinel 0 to flush the stack at the end
        
        for i in range(len(heights)):
            # While current height is shorter than the bar at stack's top
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                # This height is the shortest bar of our potential rectangle
                current_height = heights[stack.pop()]
                
                # The width is the distance between the current index (i)
                # and the new top of the stack (the next smaller bar to the left)
                current_width = i - stack[-1] - 1
                
                max_area = max(max_area, current_height * current_width)
            
            stack.append(i)
            
        # Remove the sentinel so we don't modify the input permanently
        heights.pop()
        return max_area

# Notes:
# - Use a Monotonic Stack to keep track of indices of the bars in increasing order of height.
# - When a shorter bar is found, it means the rectangles formed by the taller bars in the stack cannot extend further right.
# - Pop the taller bars, calculate their area using the current index as the right boundary and the new stack top as the left boundary.
#
# Example Walkthrough: heights=[2,1,5]
# push 2. next is 1 (< 2).
# pop 2. height=2, width = i(1) - stack(-1) - 1 = 1. area=2.
# push 1, push 5...
#
# Time Complexity : O(N)
# Space Complexity: O(N) for stack
# Technique       : Monotonic Stack
# Pattern         : Largest Area