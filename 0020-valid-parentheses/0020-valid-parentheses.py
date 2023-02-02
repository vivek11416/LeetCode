class Solution:
    def isValid(self, s: str) -> bool:
        holderOpen = []
        closeToOpen = {")":"(","}":"{","]":"["}
        
        
        for c in s :
            if c in closeToOpen:
                if holderOpen and holderOpen[-1] == closeToOpen[c]:
                    holderOpen.pop()
                
                else:
                    return False
                
            else:
                holderOpen.append(c)
                
        return True if not holderOpen else False
                