class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        temp = set()
        for items in arr:
            try:
                count[items] +=1
            except:
                count[items] =1
                
        for _,v in count.items():
            temp.add(v)
            
        return True if len(temp) == len(count) else False
            
        