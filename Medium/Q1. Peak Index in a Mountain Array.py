class Solution:
    def peakIndexInMountainArray(self, arr):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid] > arr[mid + 1]:
                high = mid
        return low

# Notes:
# - Use Binary Search to find the peak by comparing mid element with the next element.
# - If arr[mid] < arr[mid+1], the peak is to the right (low = mid + 1).
# - If arr[mid] > arr[mid+1], the peak is to the left or at mid (high = mid).
# - The loop breaks when low == high, which converges exactly at the peak.
#
# Example Walkthrough: arr=[0,2,1,0]
# mid=1, arr[1]=2 > arr[2]=1. Peak is left/at mid. high=1.
# low=0, high=1 -> mid=0. arr[0]=0 < arr[1]=2. low=1. Loop ends.
#
# Time Complexity : O(log N)
# Space Complexity: O(1)
# Technique       : Binary Search
# Pattern         : Find Maximum/Peak