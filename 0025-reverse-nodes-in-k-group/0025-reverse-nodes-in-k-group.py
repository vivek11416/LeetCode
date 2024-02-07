# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self,curr,k):
        while curr and k:
            curr=curr.next
            k -= 1

        return curr
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy
        
        
        while True:
            kth = self.getKthNode(groupPrev,k) 
            if not kth:
                break
            
            groupNext = kth.next
            
            prev , curr = kth.next,groupPrev.next
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev=curr
                curr = temp
                
            temp =  groupPrev.next   
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
        
