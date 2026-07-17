class Solution(object):

    def merge(self, left, right):
        ans = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        ans.extend(left[i:])
        ans.extend(right[j:])

        return ans

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def sortArray(self, nums):
        return self.mergeSort(nums)