class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxNum = 0
        
        for ind in range(len(number)):
            if list(number)[ind] == digit:
                maxNum = max(maxNum,int("".join(list(number)[:ind])+"".join(list(number)[ind+1:])))
                
        return str(maxNum)
        