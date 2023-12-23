# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if pos == -1:
            return false
        
        else:
            countMap = set()
            cur = head
            
            while cur:
                if cur in countMap:
                    return True
                else:
                    countMap.add(cur)
                    
                cur = cur.next
                
            return False
        