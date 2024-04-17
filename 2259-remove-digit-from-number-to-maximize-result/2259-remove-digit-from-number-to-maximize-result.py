class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxNum = 0
        origList = list(number)
        
        for ind in range(len(number)):
            if list(number)[ind] == digit:
                maxNum = max(maxNum,int("".join(origList[:ind])+"".join(origList[ind+1:])))
                
        return str(maxNum)
        