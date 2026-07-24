class Solution(object):

    def merge(self, left, right):
        ans = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        ans.extend(left[i:])
        ans.extend(right[j:])

        return ans

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def sortArray(self, nums):
        return self.mergeSort(nums)

# Notes:
# - Divide and conquer approach using Merge Sort.
# - Recursively split the array in half until base case (size <= 1) is reached.
# - Merge sorted halves using two pointers (i, j) to build a new sorted array.
# - Extend remaining elements from left or right if one pointer finishes early.
#
# Example Walkthrough: nums=[5,2,3,1]
# Split: [5,2] and [3,1] -> [5],[2] and [3],[1]
# Merge: [2,5] and [1,3] -> Compare elements to form [1,2,3,5]
#
# Time Complexity : O(N log N)
# Space Complexity: O(N)
# Technique       : Merge Sort
# Pattern         : Divide and Conquer