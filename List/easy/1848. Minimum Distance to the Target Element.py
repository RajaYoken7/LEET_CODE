class Solution(object):
    def getMinDistance(self, nums, target, start):
        ans = float('inf')  
        
        for i in range(len(nums)):
            if nums[i] == target:
                a = abs(i - start)
                if a < ans:
                    ans = a
                    
        return ans
