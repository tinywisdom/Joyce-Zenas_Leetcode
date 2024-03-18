# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createpath(node_lst):
        path = str(node_lst[0].val)
        for i in range(1, len(node_lst)):
            path = path + "->" + str(node_lst[i].val)
        return path

    # 注意！！这里path_lst是地址传递，但是node_lst是值传递
    def recursive(root: Optional[TreeNode], node_lst, path_lst):
        node_lst.append(root)
        # 叶子结点
        if root.left is None and root.right is None:
            path_lst.append(Solution.createpath(node_lst))
            return 
        # 左节点
        if root.left is not None:
            Solution.recursive(root.left, [j for j in node_lst], path_lst)
        # 右节点
        if root.right is not None:
            Solution.recursive(root.right, [j for j in node_lst], path_lst)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        Solution.recursive(root, [], res)
        return res
