class Solution(object):
    def minSubarray(self, nums, p):
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        mp = {0: -1}
        prefix = 0
        res = len(nums)
        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix - target + p) % p
            if need in mp:
                res = min(res, i - mp[need])
            mp[prefix] = i
        return -1 if res == len(nums) else res

# Notes:
# - Calculate total sum modulo p to find the target remainder we need to remove (`target`).
# - If target is 0, the array is already divisible.
# - Use a hash map to store `(prefix_sum % p) -> index`.
# - At each step, calculate the required previous prefix sum (`need`) such that removing the subarray between `need` and current prefix sum gives the `target` remainder.
#
# Example Walkthrough: nums=[3,1,4,2], p=6. total=10, target=4.
# mp={0:-1}. i=0, x=3: prefix=3, need=(3-4+6)%6=5. mp={0:-1, 3:0}.
# i=1, x=1: prefix=4, need=(4-4+6)%6=0. Found 0 at -1. res = min(len, 1 - (-1)) = 2.
#
# Time Complexity : O(N)
# Space Complexity: O(N) for hash map
# Technique       : Prefix Sum / Hash Map
# Pattern         : Subarray Remainder