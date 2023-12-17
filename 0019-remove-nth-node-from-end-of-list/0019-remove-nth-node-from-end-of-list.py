# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_LL = ListNode(0,head)
        left = new_LL
        right = head
        
        while n>0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return new_LL.next
            