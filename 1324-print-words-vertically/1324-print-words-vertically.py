class Solution:
    def printVertically(self, s: str) -> List[str]:
        listOfWords = s.split()
        maxLen = max(listOfWords, key = len)
        ans = []
        for j in range(len(maxLen)):
            tempAns = []
            for i in range(len(listOfWords)):
                try:
                    tempAns.append(listOfWords[i][j])
                except:
                    tempAns.append(" ")
            
            ans.append(''.join(tempAns).rstrip())   
            
        return ans
            
        