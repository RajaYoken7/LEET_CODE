def fourSum(self, nums, target):
    nums.sort()
    results = []
    self.findNsum(nums, target, 4, [], results)
    return results

def findNsum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2: return

    # solve 2-sum
    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):   # careful about range
            if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    return

# Notes:
# - Generalized N-Sum approach using recursion, reducing N down to 2-Sum.
# - Sort array to handle duplicates easily and optimize with early breaking.
# - For N=2, use standard two-pointer technique on sorted array.
# - Important Pruning: Break early if target is impossible (target < min_possible or target > max_possible).
# - Skip duplicate elements to avoid duplicate quadruplets.
#
# Example Walkthrough: nums=[1,0,-1,0,-2,2], target=0
# Sort: [-2,-1,0,0,1,2]. N=4. Pick -2, recurse N=3 (target=2).
# Pick -1, recurse N=2 (target=3). Two pointers find [1,2]. Result: [-2,-1,1,2].
#
# Time Complexity : O(N^(k-1)) -> O(N^3) for 4Sum
# Space Complexity: O(N) for recursion stack
# Technique       : Two Pointers + Recursion
# Pattern         : K-Sum / Generalized N-Sum