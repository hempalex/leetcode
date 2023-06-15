# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        prev = None
        min_diff = float('inf')

        def inorder(root: Optional[TreeNode]):
            nonlocal prev, min_diff

            if not root:
                return

            inorder(root.left)
            if prev:
                min_diff = min(min_diff, root.val - prev.val)
            prev = root
            inorder(root.right)

        inorder(root)
        
        return min_diff