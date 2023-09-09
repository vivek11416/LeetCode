class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {"b":0,"a":0,"l":0,"o":0,"n":0}
        textList = list(text)
        temp = []
        
        for val in textList:
            try:
                count[val] +=1
            except:
                continue
        
        for k,v in count.items():
            if k == "l" or k=="o":
                temp.append(v//2)
            else:
                temp.append(v)

                
        return min(temp)
                
        