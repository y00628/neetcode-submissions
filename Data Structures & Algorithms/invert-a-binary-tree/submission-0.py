# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def reassign(node):
            if node is None:
                return 

            node.left, node.right = node.right, node.left

            reassign(node.left)
            reassign(node.right)

        reassign(root)

        return root