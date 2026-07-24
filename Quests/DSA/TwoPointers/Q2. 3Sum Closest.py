class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort the array to use the two-pointer technique
        nums.sort()
        n = len(nums)
        # Initialize closest_sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # xrange is preferred over range in Python 2 for memory efficiency
        for i in xrange(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find the exact target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
