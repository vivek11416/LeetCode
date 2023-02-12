class Solution:
    def sortSentence(self, s: str) -> str:
        #"is2 sentence4 This1 a3"
        #is2   2+is 2is
        arra = [i[-1] + i[:-1] for i in s.split()]
        
        arra.sort()
        
        ans=""
        for i in arra:
            ans += i[1:] + " "
        
        return ans[:-1]
    
            
        