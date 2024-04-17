# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = placeHolderNode = ListNode(0)
        curr = head.next
        temp = 0
        while curr:
            
            while curr.val != 0:
                temp += curr.val          
                curr = curr.next
                
            else:
                placeHolderNode.next = ListNode(temp)
                placeHolderNode = placeHolderNode.next
                temp=0
                curr = curr.next
                
        return result.next
        