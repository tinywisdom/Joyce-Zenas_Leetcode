# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def CreateNode(rootnode, inorder_lst, preorder_lst):
        if len(inorder_lst) == 0:
            return
        inorder_index = inorder_lst.index(rootnode.val) # 查找根节点在inorder中所在位置
        preorder_index = preorder_lst.index(rootnode.val) # 查找根节点在preorder中所在位置
        left_tree = inorder_lst[:inorder_index] # 左子树
        right_tree = inorder_lst[inorder_index+1:] # 右子树
        if len(left_tree) != 0:
            rootnode.left = TreeNode(preorder_lst[preorder_index+1], None, None)
            Solution.CreateNode(rootnode.left, left_tree, preorder_lst)
        if len(right_tree) != 0:
            rootnode.right = TreeNode(preorder_lst[preorder_index+len(left_tree)+1], None, None)
            Solution.CreateNode(rootnode.right, right_tree, preorder_lst)
        

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0], None, None)
        Solution.CreateNode(root, inorder, preorder)
        return root
        