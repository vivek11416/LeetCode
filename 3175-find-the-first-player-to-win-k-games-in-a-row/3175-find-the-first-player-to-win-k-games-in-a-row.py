class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        if k>len(skills):
            return skills.index(max(skills))
        
        
        maxi = 0
        player = 0
        for i in range(1,len(skills)):

            if skills[maxi] < skills[i]:
                maxi = i
                player = 1
            else:
                player += 1

            if player == k:
                return maxi
                
        return maxi
            

        