# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        self.count = 0

        def postorder(node):
            if node is None:
                return (0, 0)  # (sum, count) of an empty subtree

            left_sum, left_count = postorder(node.left)
            right_sum, right_count = postorder(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            average = total_sum // total_count
            if average == node.val:
                self.count += 1

            return (total_sum, total_count)  # pass this subtree's info up

        postorder(root)
        return self.count
