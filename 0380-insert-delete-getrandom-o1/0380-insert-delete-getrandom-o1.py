class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        
        

    def insert(self, val: int) -> bool:
        flag = val not in self.numMap
        if flag:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return flag
        

    def remove(self, val: int) -> bool:
        flag = val in self.numMap
        if flag:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]      
        return flag
        #{1:0,3:2,4:1}
        #[1,4,3]
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()