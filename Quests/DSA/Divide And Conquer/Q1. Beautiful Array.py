class Solution:
    def beautifulArray(self, n):
        ans = [1]

        while len(ans) < n:
            temp = []

            for x in ans:
                if 2 * x - 1 <= n:
                    temp.append(2 * x - 1)

            for x in ans:
                if 2 * x <= n:
                    temp.append(2 * x)

            ans = temp

        return ans

# Notes:
# - Divide and conquer strategy based on properties of arithmetic sequences.
# - If we split numbers into odds and evens, `odd + even = odd`, which cannot equal `2 * mid` (even).
# - We can build a beautiful array of size `n` by generating a smaller beautiful array and mapping it to odds (`2x - 1`) and evens (`2x`).
#
# Example Walkthrough: n=4
# ans=[1]
# temp (odds): 2(1)-1=1. temp (evens): 2(1)=2. ans=[1,2]
# temp (odds): 2(1)-1=1, 2(2)-1=3. (evens): 2(1)=2, 2(2)=4. ans=[1,3,2,4].
#
# Time Complexity : O(N log N)
# Space Complexity: O(N)
# Technique       : Divide and Conquer / Array Construction
# Pattern         : Beautiful Array