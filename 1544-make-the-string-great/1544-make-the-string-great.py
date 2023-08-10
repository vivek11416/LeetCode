class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        s = list(s)
        while i <len(s)-1:
            if s[i].lower() == s[i+1].lower() and((s[i].isupper() and s[i+1].islower()) or (s[i].islower() and s[i+1].isupper())):
                s.pop(i)
                s.pop(i)
                
                i -= 1 if i>0 else 0
                continue
            
            i += 1
        
        return "".join(s)
                
                

