import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        res = []
        if not nums1 or not nums2 or k == 0:
            return res
        
        # Min-Heap stores: (sum, index_in_nums1, index_in_nums2)
        min_heap = []
        
        # 1. Initialise the heap with the first k possible pairs 
        # (nums1[i], nums2[0])
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            
        # 2. Extract the smallest sum and add the next potential pair
        while min_heap and len(res) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            
            # If there is a next element in nums2 for the current nums1[i], push it
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return res

# Notes:
# - Use a Min-Heap to find the K smallest pairs efficiently without generating all pairs.
# - Initially, push `(nums1[i] + nums2[0], i, 0)` for `i` up to `k` into the heap.
# - The heap allows us to always extract the current smallest sum pair.
# - After extracting `(sum, i, j)`, if there's a next element in `nums2` (`j+1`), push `(nums1[i] + nums2[j+1], i, j+1)`.
#
# Example Walkthrough: nums1=[1,7,11], nums2=[2,4,6], k=3
# heap=[ (3, 0, 0), (9, 1, 0), (13, 2, 0) ]
# pop (3): pair=[1,2]. push (1+4, 0, 1)=(5,0,1).
# pop (5): pair=[1,4]. push (1+6, 0, 2)=(7,0,2).
# pop (7): pair=[1,6]. push nothing (j=2 is last).
#
# Time Complexity : O(K log(min(K, N)))
# Space Complexity: O(min(K, N)) for heap
# Technique       : Priority Queue / Min-Heap
# Pattern         : Kth Smallest Element / Merge K Sorted