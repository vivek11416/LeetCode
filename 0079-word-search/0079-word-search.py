class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0] and self.search(board,y,x ,0, word):
                    return True
        return False
    
    def search(self,board,y,x,indx,word):
        if indx==len(word):
            return True
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]) or board[y][x] != word[indx]:
            return False
        
        temp = board[y][x]
        board[y][x] = " "
        found = self.search(board,y+1,x,indx+1,word) or self.search(board,y-1,x,indx+1,word) or self.search(board,y,x+1,indx+1,word) or self.search(board,y,x-1,indx+1,word) 
        board[y][x] = temp
        return found