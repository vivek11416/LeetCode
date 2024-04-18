class Solution:
    def checkString(self, s: str) -> bool:
        allChar = list(s)
        
        for i in range(1,len(allChar)):
            if allChar[i] == 'a' and allChar[i-1]=='b':
                return False
            
        return True
            
        