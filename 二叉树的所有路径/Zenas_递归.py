# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def listTostr(path: List) -> str:
        if len(path) == 1:
            return str(path[0])
        else:
            res = ""
            for i in range(len(path) - 1):
                res = res + str(path[i]) + "->"
            res = res + str(path[len(path) - 1])
            return res

    def getPath(root: Optional[TreeNode], current_path: List, result_paths: List):
        if root is None:
            return
        current_path.append(root.val)
        if root.left is None and root.right is None:
            result_paths.append(current_path)
            return
        else:
            if root.left is not None:
                Solution.getPath(root.left, [j for j in current_path], result_paths)
            if root.right is not None:
                Solution.getPath(root.right, [j for j in current_path], result_paths)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res_path = []
        current_path = []
        Solution.getPath(root, current_path, res_path)
        res = []
        for path in res_path:
            res.append(Solution.listTostr(path))
        
        return res