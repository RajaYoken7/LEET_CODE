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
        
