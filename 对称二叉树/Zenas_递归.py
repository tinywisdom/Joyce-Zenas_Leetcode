# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(leftRoot: Optional[TreeNode], rightRoot: Optional[TreeNode]) -> bool:
        if leftRoot is None and rightRoot is None:
            return True
        elif leftRoot is None or rightRoot is None:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        else:
            return Solution.isSame(leftRoot.left, rightRoot.right) and Solution.isSame(leftRoot.right, rightRoot.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution.isSame(root.left, root.right)