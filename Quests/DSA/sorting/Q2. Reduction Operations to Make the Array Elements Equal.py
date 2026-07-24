class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        operations = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1
            operations += count
        return operations

# Notes:
# - Sort the array. The largest elements need to be reduced to the next largest, cascading down to the minimum.
# - Maintain a `count` of how many distinct strictly smaller elements exist before the current element.
# - Each time the number changes (e.g., we move to a larger number), increment `count`.
# - Add this `count` to the total operations, as this element (and all elements equal to it) will need `count` reductions to reach the minimum.
#
# Example Walkthrough: nums=[1,1,2,2,3]
# sort=[1,1,2,2,3]. count=0.
# i=1 (1): ==, ops=0.
# i=2 (2): != (1), count=1, ops=0+1=1.
# i=3 (2): ==, ops=1+1=2.
# i=4 (3): != (2), count=2, ops=2+2=4.
#
# Time Complexity : O(N log N)
# Space Complexity: O(1) or O(N) for sort
# Technique       : Sorting / Counting
# Pattern         : Array Reduction