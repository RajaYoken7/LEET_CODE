class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        operations = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1
            operations += count
        return operations