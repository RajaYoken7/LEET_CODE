class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

# Notes:
# - Kadane's Algorithm: Maintain a running sum (`curr_sum`).
# - At each step, decide whether to add the current element to the running sum, or start a new subarray from the current element.
# - Keep track of the maximum sum seen so far (`max_sum`).
#
# Example Walkthrough: nums=[-2, 1, -3, 4]
# i=0: curr=-2, max=-2
# i=1: curr=max(1, -2+1) = 1, max=1
# i=2: curr=max(-3, 1-3) = -2, max=1
# i=3: curr=max(4, -2+4) = 4, max=4
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Kadane's Algorithm (Dynamic Programming)
# Pattern         : Maximum Subarray
