class Solution:
    def isValid(self, s: str) -> bool:
        validDict = {')':'(','}':'{',']':'['}
        stack = []
        
        for val in s:
            if stack and val in validDict and stack[-1] == validDict[val] :
                stack.pop()
            else:
                stack.append(val)
                
        return False if stack else True
            
        