class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s) 
        stack = []
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
                    
        for i in stack:
            s[i] = ""
            
        return "".join(s)