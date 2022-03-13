class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def get_next_row(current_row):
            return (current_row + 1) % 2
        
        def is_obstacle(obstacleGrid, i, j):
            return obstacleGrid[i][j] == 1
        
        # if the goal is contains an obstacle
        if is_obstacle(obstacleGrid, -1, -1):
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        n_paths = [[0 for j in range(n)] for i in range(2)]
        current_row = 0
        i_row = m - 1
        
        # initialize final row
        n_paths[current_row][-1] = 1
        for j in reversed(range(n)):
            if j + 1 < n:
                if is_obstacle(obstacleGrid, i_row, j):
                    continue
                if not is_obstacle(obstacleGrid, i_row, j + 1):
                    n_paths[current_row][j] = n_paths[current_row][j + 1]
                else:
                    n_paths[current_row][j] = 0
        current_row = get_next_row(current_row)        
        i_row -= 1
        
        while i_row >= 0:
            for j in reversed(range(n)):
                if is_obstacle(obstacleGrid, i_row, j):
                    continue
                another_row = get_next_row(current_row)
                n_paths[current_row][j] = 0
                # right
                if j + 1 < n and not is_obstacle(obstacleGrid, i_row, j + 1):
                    n_paths[current_row][j] += n_paths[current_row][j + 1]
                # down
                if not is_obstacle(obstacleGrid, i_row + 1, j):
                    n_paths[current_row][j] += n_paths[another_row][j]
                
            current_row = get_next_row(current_row)
            i_row -= 1
        
        return n_paths[get_next_row(current_row)][0]
        