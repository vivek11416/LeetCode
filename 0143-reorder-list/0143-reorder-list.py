# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp,fp = head,head.next
        while fp and fp.next:
            sp=sp.next
            fp=fp.next.next
            
        
        h2 = sp.next
        sp.next = None
        rev_list = None
        
        
        while h2:
            temp = h2.next
            h2.next = rev_list
            rev_list = h2
            h2 = temp
            
        h1 , h2 = head,rev_list
        
        while h2:
            temp1,temp2 = h1.next,h2.next
            h1.next = h2
            h2.next = temp1
            h1,h2 = temp1,temp2