class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Edge case: impossible bc start or end cell isn't clear
        if grid[0][0] or grid[-1][-1]:
            return -1
        # Edge case: single cell
        if grid == [[0]]:
            return 1

        # (x, y, path length)
        q = [(0, 0, 1)]
        # Mark start as visited
        grid[0][0] = 1

        # BFS
        while q:
            x, y, length = q.pop(0)

            # Check neighboring cells
            for nextX in [x-1, x, x+1]:
                for nextY in [y-1, y, y+1]:
                    # Answer found
                    if nextX == len(grid) - 1 and nextY == len(grid[0]) - 1:
                        return length + 1
                    
                    # Add next coordinate to next queue if the cell is clear
                    if 0 <= nextX and nextX < len(grid) and 0 <= nextY and nextY < len(grid[0]):
                        if grid[nextX][nextY] == 0:
                            q.append((nextX, nextY, length + 1))
                            # Mark as visited
                            grid[nextX][nextY] = 1

        return -1