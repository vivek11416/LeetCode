class Solution:
    import math
    def evalRPN(self, tokens: List[str]) -> int:
        
        tempLis = tokens
        
        while len(tempLis)>1:
            for i in range(len(tempLis)):
                if tempLis[i] in ['+', '-', '*','/']:
                    tempLis[i-2] = math.trunc(float(eval(str(tempLis[i-2])+ str(tempLis[i])+str(tempLis[i-1]))))
                    
                    tempLis.pop(i-1)
                    tempLis.pop(i-1)
                    break
        
        return int(tempLis[0])
        