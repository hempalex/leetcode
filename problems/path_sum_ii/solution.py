# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def dfs(root: Optional[TreeNode], lst: List[int] = []):

            if not root.left and not root.right:
                if sum(lst) + root.val == targetSum:
                    res.append(lst + [root.val])
                return



            if root.left: dfs(root.left, lst + [root.val])
            if root.right: dfs(root.right, lst + [root.val])

        if root: dfs(root)

        return res