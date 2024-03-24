# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        i = 0
        start_node = head
        while start_node:
            if start_node not in dic:
                dic[start_node] = i
                i = i + 1
                start_node = start_node.next
            else:
                return start_node
        
        return

        