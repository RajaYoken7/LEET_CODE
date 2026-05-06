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