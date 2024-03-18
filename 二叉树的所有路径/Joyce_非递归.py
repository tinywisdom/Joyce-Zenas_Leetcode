# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 栈 dfs
        path_res = [] # 从根节点到叶子节点的路径
        stack_node = [] # 存放节点
        flag = [] # 存放对应每个节点的左右孩子是否被遍历过
        stack_node.append(root)
        if root.left is not None:
            flag.append(0)
        else:
            flag.append(-1)
        if root.right is not None:
            flag.append(0)
        else:
            flag.append(-1)        

        while len(stack_node) != 0:
            current_node = stack_node[-1] 
            flag_left = flag[(len(stack_node)-1) * 2]
            flag_right = flag[(len(stack_node)-1) * 2 + 1]
            # 两个都是-1，无路可走，回溯
            if flag_left == -1 and flag_right == -1:
                res = str(stack_node[0].val)
                for k in range(1, len(stack_node)):
                    res = res + "->" + str(stack_node[k].val)
                path_res.append(res)
                stack_node = stack_node[:-1]
                flag = flag[:-2]
            # 左孩子没有遍历过
            elif flag_left == 0:
                flag[(len(stack_node)-1) * 2] = 1
                stack_node.append(current_node.left)               
                if current_node.left.left is not None:
                    flag.append(0)
                else:
                    flag.append(-1)
                if current_node.left.right is not None:
                    flag.append(0)
                else:
                    flag.append(-1)   
            # 右孩子没有遍历过
            elif flag_right == 0:
                flag[(len(stack_node)-1) * 2 + 1] = 1
                stack_node.append(current_node.right)               
                if current_node.right.left is not None:
                    flag.append(0)
                else:
                    flag.append(-1)
                if current_node.right.right is not None:
                    flag.append(0)
                else:
                    flag.append(-1)    
            # 左孩子和右孩子都遍历过了
            else:
                stack_node = stack_node[:-1]              
                flag = flag[:-2]
        return path_res



            
        