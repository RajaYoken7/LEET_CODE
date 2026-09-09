class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stores indices
        
        for i in range(n):
            # While stack is not empty and current temp is warmer than the temp 
            # at the index on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # Calculate the distance between days
                answer[prev_index] = i - prev_index
            
            # Push the current index onto the stack
            stack.append(i)
            
        return answer

# Notes:
# - Use a Monotonic Stack to store indices of days where we haven't found a warmer day yet.
# - Iterate through temperatures. If the current day is warmer than the day at the top of the stack, pop the stack.
# - Calculate the difference in indices to get the number of days waited, and update the answer array.
#
# Example Walkthrough: temps=[73, 74, 75]
# i=0 (73): stack=[0]
# i=1 (74): 74 > 73. pop 0. ans[0] = 1-0 = 1. stack=[1]
# i=2 (75): 75 > 74. pop 1. ans[1] = 2-1 = 1. stack=[2]
#
# Time Complexity : O(N)
# Space Complexity: O(N) for stack
# Technique       : Monotonic Stack
# Pattern         : Next Greater Element