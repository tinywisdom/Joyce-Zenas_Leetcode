# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isdelete(root: Optional[TreeNode], left_node: Optional[TreeNode], right_node: Optional[TreeNode]):
        # 是叶子结点
        if left_node is None and right_node is None:
            if root.val == 0:
                return True
            else:
                return False
        
        # 左子树
        if left_node is not None:
            left_flag = Solution.isdelete(root.left, root.left.left, root.left.right)
            if left_flag:
                root.left = None
        else:
            left_flag = True

        # 右子树
        if right_node is not None:
            right_flag = Solution.isdelete(root.right, root.right.left, root.right.right)
            if right_flag:
                root.right = None        
        else:
            right_flag = True  

        if left_flag and right_flag and root.val == 0:
            return True
        else:
            return False

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        flag = Solution.isdelete(root, root.left, root.right)
        if flag:
            root = None
        return root
        