from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = defaultdict(int)
        
        for char in s1:
           s1Dict[char]  += 1
        
        print(s1Dict)
        l=0
        r=l+(len(s1))
        
        while r <= len(s2)+1:
            s2Dict = defaultdict(int)
            for char in s2[l:r]:
                s2Dict[char]+=1
            print(s2Dict)
            if s1Dict == s2Dict:
                return True
            
            else:
                
                l += 1
                r +=1
                
                
        
        return False
        
        