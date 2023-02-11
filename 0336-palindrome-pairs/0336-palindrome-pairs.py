class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backwards , res = {},[]
        
        for i, word in enumerate(words):
            backwards[word[::-1]] = i
            
        for i , word in enumerate(words):
            
            if word in backwards and backwards[word] != i:
                res.append([i,backwards[word]])
                
            if word !="" and "" in backwards and word == word[::-1]:
                res.append([i,backwards[""]])
                res.append([backwards[""],i])
                
            for j in range(len(word)):
                if word[j:] in backwards and word[:j] == word[j-1::-1]:
                    res.append([backwards[word[j:]],i])
                    
                if word[:j] in backwards and word[j:] == word[:j-1:-1]:
                    res.append([i,backwards[word[:j]]])
                    
        return res
                
                
        #O(n.w^2)
        