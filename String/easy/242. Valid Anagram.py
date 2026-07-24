class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

# Notes:
# - By definition, an anagram has the exact same characters with the same frequencies.
# - Sorting both strings guarantees that if they are anagrams, they will become identical strings (or lists).
# - A more optimal O(N) approach would use a HashMap or fixed-size array to count character frequencies.
#
# Example Walkthrough: s="anagram", t="nagaram"
# sorted(s) = ['a','a','a','g','m','n','r']
# sorted(t) = ['a','a','a','g','m','n','r']
# They match -> True.
#
# Time Complexity : O(N log N)
# Space Complexity: O(N) for sorting
# Technique       : Sorting
# Pattern         : String Comparison
