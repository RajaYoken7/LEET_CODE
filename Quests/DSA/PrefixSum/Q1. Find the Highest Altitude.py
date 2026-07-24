class Solution(object):
    def largestAltitude(self, gain):
        currentAltitude = 0
        maxAltitude = 0
        for i in gain:
            currentAltitude += i
            if currentAltitude > maxAltitude:
                maxAltitude=currentAltitude
        return maxAltitude

# Notes:
# - Start at altitude 0.
# - Iterate through the `gain` array, adding each gain to the `currentAltitude` to find the altitude at the next point.
# - Keep track of the `maxAltitude` seen so far.
#
# Example Walkthrough: gain=[-5,1,5,0,-7]
# start=0. max=0.
# i=-5: alt=-5. max=0
# i=1: alt=-4. max=0
# i=5: alt=1. max=1
#
# Time Complexity : O(N)
# Space Complexity: O(1)
# Technique       : Prefix Sum
# Pattern         : Running Total