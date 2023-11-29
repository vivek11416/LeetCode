class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(posSpeed)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
                
        return len(stack)