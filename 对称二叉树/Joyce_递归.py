# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(left_treenode, right_treenode):
        if left_treenode is None and right_treenode is None:
            return 1
        elif left_treenode is None or right_treenode is None:
            return 0
        elif left_treenode.val == right_treenode.val:
            flag_left = Solution.recursive(left_treenode.left, right_treenode.right)
            flag_right = Solution.recursive(left_treenode.right, right_treenode.left)
            if flag_left == 1 and flag_right == 1:
                return 1
            else:
                return 0
        else:
            return 0
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        elif Solution.recursive(root.left, root.right) == 1:
            return True
        else:
            return False
