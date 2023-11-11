from collections import defaultdict  
class TimeMap:
    
    def __init__(self):
        self.valueMap = {}
        self.keytimeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.valueMap[(key,timestamp)] = value
        self.keytimeMap[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        selList = self.keytimeMap[key]
        l,r  = 0 , len(selList)-1
        ans =None
        if not selList or timestamp < selList[0]:
            return ""
        
        while l<=r:
            m=(l+r)//2
            if timestamp>selList[m]:
                l = m+1
            
            elif timestamp<selList[m]:
                r = m-1
                
            else:
                ans = selList[m]
                break
                
        if not ans:
            ans = selList[l-1]
            
        return self.valueMap[(key,ans)]
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)