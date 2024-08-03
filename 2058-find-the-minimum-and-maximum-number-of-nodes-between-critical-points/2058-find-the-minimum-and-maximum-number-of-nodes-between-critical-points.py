# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def critical(prev,cur,nextn):
            return (prev.val>cur.val<nextn.val or prev.val<cur.val>nextn.val)
        
        prev,curr = head,head.next
        nextn = curr.next
        loc_min,loc_max = float("inf"),float("-inf")
        pci = 0
        fci = 0
        i=1
        while nextn:
            
            if critical(prev,curr,nextn):
                if fci:
                    loc_max = i - fci
                    loc_min = min(loc_min,i-pci)
                    
                else:
                    fci = i
                pci = i
            
            
            prev,curr,nextn = curr,nextn,nextn.next
            i+=1
        if  loc_min== float("inf"): return [-1,-1]
        return [loc_min,loc_max]
            
         