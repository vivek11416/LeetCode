class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()
        lef , rig = 0,len(products) - 1
        
        for i in range(len(searchWord)):
            c = searchWord[i]
            
            while lef <= rig and (len(products[lef]) <= i or (products[lef][i] != c)):
                lef += 1
            
            while lef <= rig and (len(products[rig]) <= i or products[rig][i] != c):
                rig -= 1
                
            
            ans.append(products[lef:min(lef+3,rig+1)])
        
        return ans