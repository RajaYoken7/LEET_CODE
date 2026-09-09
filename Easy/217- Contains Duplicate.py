class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

# Notes:
# - Convert the list to a set, which automatically removes any duplicate elements.
# - Compare the length of the set to the length of the original list.
# - If the lengths differ, it means duplicates were removed, so return True.
#
# Example Walkthrough: nums=[1,2,3,1]
# len(nums) = 4
# set(nums) = {1,2,3}, len = 3
# 4 != 3 -> True (Contains duplicate).
#
# Time Complexity : O(N)
# Space Complexity: O(N) to store the set
# Technique       : HashSet
# Pattern         : Duplicate Detection
