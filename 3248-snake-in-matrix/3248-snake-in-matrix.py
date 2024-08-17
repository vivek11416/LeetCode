class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        moveMap = {'DOWN':(1,0),
                  'UP':(-1,0),
                  'RIGHT':(0,1),
                  'LEFT':(0,-1)}
        cPos = 0
        i,j = 0,0
        for val in commands:
            i += moveMap[val][0]
            j += moveMap[val][1]
            
            cPos = (i * n) + j
            
        return cPos
            
        