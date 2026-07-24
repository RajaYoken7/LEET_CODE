class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if ((len(nums1))%2==0):
            a=len(nums1)//2
            return (nums1[a-1]+nums1[a])/2.0
        b=len(nums1)//2
        return nums1[b]

# Notes:
# - Brute-force approach: Merge both arrays and sort them.
# - If the total length is even, find the average of the two middle elements.
# - If the total length is odd, return the middle element.
# - This does not achieve the optimal O(log(m+n)) time complexity.
#
# Example Walkthrough: nums1=[1,3], nums2=[2]
# Merged: [1,2,3]. Length=3 (odd).
# b = 3//2 = 1. return nums1[1] (2).
#
# Time Complexity : O((M+N) log(M+N)) due to sorting
# Space Complexity: O(M+N) for storing merged array elements
# Technique       : Sorting
# Pattern         : Array Merge
        
