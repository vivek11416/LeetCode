class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordsmap = Counter(words[0])
        
        for word in words:
            wordsmap &= Counter(word)
            
        return wordsmap.elements()