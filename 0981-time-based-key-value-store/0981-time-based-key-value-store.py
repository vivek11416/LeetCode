class TimeMap:

    def __init__(self):
        self.keyTimestamp = {}
        self.keyValueList = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTimestamp[(key,timestamp)]=value
        self.keyValueList[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        tiStLis = self.keyValueList[key]
        if not tiStLis or tiStLis[0]>timestamp:
            return ""
        
        l = 0
        r = len(tiStLis)-1
        
        while l<=r:
            m = (l+r)//2
            if tiStLis[m] == timestamp:
                return self.keyTimestamp[(key,tiStLis[m])]
            elif timestamp<tiStLis[m]:
                r = m-1
            elif timestamp>tiStLis[m]:
                l = m+1
        return self.keyTimestamp[(key,tiStLis[l-1])]
        
                
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)