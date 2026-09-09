class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == len(set(nums)):
            return False
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False

# Notes:
# - Use a dictionary to store the most recent index of each number.
# - Traverse the array once using enumerate().
# - If the current number is already in the dictionary, check the index difference.
# - If (current_index - previous_index) <= k, a nearby duplicate is found.
# - Otherwise, update the dictionary with the current index.
# - Storing the latest index ensures we always compare with the closest occurrence.
# - Initial check (len(nums) == len(set(nums))) quickly returns False if no duplicates exist.

# Example:
# nums = [1,2,3,1], k = 3
# i = 3, previous index of 1 = 0
# 3 - 0 = 3 <= k -> Return True

# Time Complexity : O(n)
# Space Complexity: O(n)
# Technique        : Hash Map / Single Pass
# Pattern          : Store Last Seen Index