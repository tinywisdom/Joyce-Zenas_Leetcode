# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMin(root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp
    def getMax(root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root
        while temp.right is not None:
            temp = temp.right
        return temp
    def _isValidBST(root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        elif root.left is None:
            return Solution._isValidBST(root.right) and root.val < Solution.getMin(root.right).val
        elif root.right is None:
            return Solution._isValidBST(root.left) and root.val > Solution.getMax(root.left).val
        else:
            return Solution._isValidBST(root.left) and Solution._isValidBST(root.right) and root.val < Solution.getMin(root.right).val and root.val > Solution.getMax(root.left).val
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution._isValidBST(root)
        