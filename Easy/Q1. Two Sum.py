class Solution(object):
    def twoSum(self, nums, target):
        numMap={}
        for i,num in enumerate(nums):
            complement=target - num
            if complement in numMap:
                return[numMap[complement],i]
            numMap[num]=i

# Notes:
# - Use a hash map to store each number and its index as we iterate.
# - For each number, calculate its complement (target - num).
# - If the complement exists in the map, we found the pair; return their indices.
# - This avoids the O(N^2) nested loop by using O(1) map lookups.
#
# Example Walkthrough: nums=[2,7,11,15], target=9
# i=0, num=2: comp=7. Not in map. Map={2:0}
# i=1, num=7: comp=2. In map! Return [0,1]
#
# Time Complexity : O(N)
# Space Complexity: O(N)
# Technique       : HashMap
# Pattern         : Two Sum / Complement Search