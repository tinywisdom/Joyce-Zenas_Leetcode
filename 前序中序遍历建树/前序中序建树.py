# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0], None, None) # 根节点
        queue = [] # 当前队列
        queue.append(root)
        flag = [0] * len(inorder) # 标记列表，标记inorder中的元素是否被遍历过
        while len(queue) != 0:
            current_node = queue[0]
            queue.pop(0)
            inorder_index = inorder.index(current_node.val) # 查找根节点在inorder中所在位置
            preorder_index = preorder.index(current_node.val) # 查找根节点在preorder中所在位置
            flag[inorder_index] = 1
            
            # 寻找左子树所包含元素的个数
            ii = inorder_index - 1
            left_num = 0
            while ii >= 0:
                if flag[ii] == 0:
                    left_num += 1
                else:
                    break
                ii -= 1
            
            # 寻找右子树所包含元素的个数
            ii = inorder_index + 1
            right_num = 0
            while ii < len(inorder):
                if flag[ii] == 0:
                    right_num += 1
                else:
                    break
                ii += 1
            
            # 获取左子树和右子树的根节点
            if left_num != 0:
                left_root = TreeNode(preorder[preorder_index+1], None, None)
                current_node.left = left_root
                queue.append(left_root)
            if right_num != 0:
                right_root = TreeNode(preorder[preorder_index+left_num+1], None, None)
                current_node.right = right_root
                queue.append(right_root)
        
        return root