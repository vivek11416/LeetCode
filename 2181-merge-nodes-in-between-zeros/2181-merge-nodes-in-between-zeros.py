# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = placeHolderNode = ListNode(0)
        curr = head.next
        
        while curr:
            temp = 0
            while curr.val != 0:
                temp += curr.val          
                curr = curr.next
                
            
            placeHolderNode.next = ListNode(temp)
            placeHolderNode = placeHolderNode.next
            curr = curr.next

        return result.next
        