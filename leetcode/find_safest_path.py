# https://leetcode.com/problems/find-the-safest-path-in-a-grid/?envType=daily-question&envId=2024-05-15
def maximumSafenessFactor(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    seen = set()

    

    def get_distance_to_thief(grid, r, c, dist):
        
        if (r,c) in set:
            return 0
        if r >= len(grid) or c >= len(grid[0]):
            return 0
        if grid[r][c] == 1:
            return dist
        
        seen.add((r,c))
        
        return min(
            [
                get_distance_to_thief(grid, r + 1, c, dist + 1),
                get_distance_to_thief(grid, r - 1, c, dist + 1),
                get_distance_to_thief(grid, r, c + 1, dist + 1),
                get_distance_to_thief(grid, r, c - 1, dist + 1),
            ]
        )
    
