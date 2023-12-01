from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        
        for i in range(0,k):
            while queue and queue[-1]<nums[i]:
                
                queue.pop()
                
            queue.append(nums[i])
        ans.append(queue[0])
        
            
        for i in range(k,len(nums)):
            if queue[0]==nums[i-k]:
                queue.popleft()
            while queue and queue[-1]<nums[i]:
                queue.pop()
                
            queue.append(nums[i])
            ans.append(queue[0])
        

        return ans