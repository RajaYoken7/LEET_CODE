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