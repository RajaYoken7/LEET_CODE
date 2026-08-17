class Solution(object):
    def findMissingElements(self, nums):
        new = []
        nums.sort()
        lowest = nums[0]
        highest = nums[-1]
        for i in range(lowest, highest + 1):
            if i not in nums:
                new.append(i)
        return new
