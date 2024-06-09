class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        if k>len(skills):
            return skills.index(max(skills))
        
        
        maxi = 0
        wins = 0
        for i in range(1,len(skills)):

            if skills[maxi] < skills[i]:
                maxi = i
                wins = 1
            else:
                wins += 1

            if wins == k:
                return maxi
                
        return maxi
            

        