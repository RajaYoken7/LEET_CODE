# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, n = 0)-> None:
            if not node: return

            n = 2 * n + node.val
            if not node.left and not node.right:
                self.ans+= n
                return
                
            dfs(node.left , n)
            dfs(node.right, n)
            return
            

        self.ans = 0
        dfs(root)
        return self.ans

# Notes:
# - Use Depth-First Search (DFS) to traverse from root to leaves.
# - Maintain the current binary value `n` by shifting it left (`2 * n`) and adding the node's value.
# - When a leaf node is reached (no left or right child), add `n` to the total sum.
# - The `n = 2 * n + node.val` trick efficiently builds the base-10 number from base-2.
#
# Example Walkthrough: Path [1, 0, 1]
# Node 1: n = 2*0 + 1 = 1
# Node 0: n = 2*1 + 0 = 2
# Node 1: n = 2*2 + 1 = 5 (Leaf, add 5 to ans)
#
# Time Complexity : O(N) where N is number of nodes
# Space Complexity: O(H) where H is tree height (recursion stack)
# Technique       : DFS
# Pattern         : Tree Traversal / Binary to Decimal
