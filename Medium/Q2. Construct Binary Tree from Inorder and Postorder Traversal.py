class Solution(object):
    def buildTree(self, inorder, postorder):
        # Base case
        if not inorder:
            return None
        
        # The last element of postorder list is the root
        root_val = postorder.pop()
        TreeNode = None
        root = TreeNode(root_val)
        
        # Find the position of the root in the inorder list
        inorder_index = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root

# Notes:
# - The last element of `postorder` is always the root of the current subtree.
# - Find this root in `inorder`. The elements to its left form the left subtree, and to its right form the right subtree.
# - Recursively build the right subtree *before* the left subtree, because we are popping from the end of `postorder` (Root-Right-Left order).
#
# Example Walkthrough: in=[9,3,15,20,7], post=[9,15,7,20,3]
# root = 3. index in `in` is 1.
# Right subtree uses in=[15,20,7], post=[9,15,7,20]
# Left subtree uses in=[9], post=[9]
#
# Time Complexity : O(N^2) (due to `.index()`), can be O(N) with HashMap
# Space Complexity: O(H) for recursion stack
# Technique       : Divide and Conquer / Recursion
# Pattern         : Tree Construction
