class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

# Notes:
# - Modified Binary Search to handle rotation.
# - One half of the array (left or right to `mid`) is always strictly sorted.
# - Check which half is sorted (`nums[l] <= nums[mid]` means left is sorted).
# - Determine if the target falls within the sorted half. If yes, search there; otherwise, search the unsorted half.
#
# Example Walkthrough: nums=[4,5,6,7,0,1,2], target=0
# l=0(4), r=6(2). mid=3(7).
# Left is sorted (4 <= 7). target 0 not in [4, 7]. l=mid+1=4.
# l=4(0), r=6(2). mid=5(1). Left is sorted (0 <= 1). target 0 in [0, 1]. r=mid-1=4.
#
# Time Complexity : O(log N)
# Space Complexity: O(1)
# Technique       : Binary Search
# Pattern         : Rotated Array