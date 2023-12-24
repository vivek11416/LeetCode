class MedianFinder:
    import math
    def __init__(self):
        self.values = []
        

    def addNum(self, num: int) -> None:
        self.values.append(num)
       

    def findMedian(self) -> float:
        
        self.values.sort()
        
        if len(self.values)%2 == 0:
            #print(self.values[int(len(self.values)/2)-1])
            return (self.values[int(len(self.values)/2)-1] + self.values[int(len(self.values)/2)])/2
        
        else:
            return (self.values[math.ceil(len(self.values)/2)-1] )
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()