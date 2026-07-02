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