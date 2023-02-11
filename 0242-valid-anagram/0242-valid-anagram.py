class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countNoS ,countNoT = {} , {}
        
        for i in range(len(s)):
            countNoS[s[i]] = 1 + countNoS.get(s[i],0)
            countNoT[t[i]] = 1 + countNoT.get(t[i],0)
        
        for c in countNoS:
            if countNoS[c] != countNoT.get(c,0):
                return False
        
        return True