# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node.val = node.next.val
        # node.next = node.next.next
        curr = node
        nextN =node.next
        
        while  nextN:
            curr.val = nextN.val
            if nextN.next is None:
                curr.next =None
                break
                
            else:
                curr= nextN
                nextN = nextN.next
        