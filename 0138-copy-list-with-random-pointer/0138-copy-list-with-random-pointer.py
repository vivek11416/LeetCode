"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None : None}
        
        cur = head
        while cur:
            new = Node(cur.val)
            oldToCopy[cur] = new
            cur = cur.next
            
        cur = head
        while cur:
            new = oldToCopy[cur]
            new.next = oldToCopy[cur.next]
            new.random = oldToCopy[cur.random]
            cur = cur.next
            
        return oldToCopy[head]
        