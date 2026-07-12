class Solution(object):
    def twoSum(self, nums, target):
        numMap={}
        for i,num in enumerate(nums):
            complement=target - num
            if complement in numMap:
                return[numMap[complement],i]
            numMap[num]=i