# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue_left = [] # 左子树待比较的队列
        queue_right = [] # 右子树待比较的队列
        if root.left is None and root.right is None:
            return True
        elif (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            return False
        elif root.left.val == root.right.val:           
            queue_left.append(root.left)
            queue_right.append(root.right)
        else:
            return False
        while len(queue_left) != 0 or len(queue_right) != 0:
            if len(queue_left) != len(queue_right):
                return False
            left_node = queue_left[0]
            right_node = queue_right[0]
            queue_left.pop(0)
            queue_right.pop(0)
            # 比较两个队列的值
            if (left_node.left is None and right_node.right is not None) or (left_node.left is not None and right_node.right is None):
                return False
            elif left_node.left is None and right_node.right is None:
                pass
            elif left_node.left.val == right_node.right.val:            
                queue_left.append(left_node.left)
                queue_right.append(right_node.right)
            else:
                return False
            
            if (left_node.right is None and right_node.left is not None) or (left_node.right is not None and right_node.left is None):
                return False
            elif left_node.right is None and right_node.left is None:
                pass
            elif left_node.right.val == right_node.left.val:            
                queue_left.append(left_node.right)
                queue_right.append(right_node.left)
            else:
                return False
            
        return True