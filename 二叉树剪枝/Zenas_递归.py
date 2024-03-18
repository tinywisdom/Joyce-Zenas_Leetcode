# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def IfUseless(root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            if root.val == 0:
                return True
            else:
                return False
        left_useless = True 
        right_useless = True
        if root.left is not None:
            left_useless = Solution.IfUseless(root.left)
        if root.right is not None:
            right_useless = Solution.IfUseless(root.right)
        if left_useless:
            root.left = None
        if right_useless:
            root.right = None
        
        return left_useless and right_useless and (root.val == 0)


    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root_useless = Solution.IfUseless(root)
        if root_useless:
            return None
        else:
            return root
