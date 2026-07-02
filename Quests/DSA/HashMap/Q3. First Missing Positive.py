class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()

        missing = 1

        for num in nums:
            if num < missing:
                continue
            elif num == missing:
                missing += 1
            else:
                break

        return missing