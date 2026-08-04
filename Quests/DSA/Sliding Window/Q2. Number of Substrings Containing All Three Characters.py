class Solution(object):
    def numberOfSubstrings(self, s):
        seen = {'a': -1, 'b': -1, 'c': -1}
        c = 0
        for i in range(len(s)):
            seen[s[i]] = i
            c += min(seen.values()) + 1
        return c

# ## Core Rule
# The lowest index in seen tells you how many valid substrings end at the current position.
# ------------------------------
# ## Trace for s = "abcabc"

# * Initial: seen = {a:-1, b:-1, c:-1}, c = 0
# * i = 0 ('a'): seen = {a:0, b:-1, c:-1} → min is -1 → c += 0 (Total: 0)
# * i = 1 ('b'): seen = {a:0, b:1, c:-1} → min is -1 → c += 0 (Total: 0)
# * i = 2 ('c'): seen = {a:0, b:1, c:2} → min is 0 → c += 1 (Total: 1)
# * Substrings: "abc"
# * i = 3 ('a'): seen = {a:3, b:1, c:2} → min is 1 → c += 2 (Total: 3)
# * Substrings: "abca", "bca"
# * i = 4 ('b'): seen = {a:3, b:4, c:2} → min is 2 → c += 3 (Total: 6)
# * Substrings: "abcab", "bcab", "cab"
# * i = 5 ('c'): seen = {a:3, b:4, c:5} → min is 3 → c += 4 (Total: 10)
# * Substrings: "abcabc", "bcabc", "cabc", "abc"

# Final Return: 10
