class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def is_valid(pos):
            nonlocal m, n
            if pos[0] < 0 or pos[0] >= m:
                return False
            if pos[1] < 0 or pos[1] >= n:
                return False
            return True
        
        def gen_valid_next(cur_pos, cur_val, matrix):
            all_next_pos = []
            for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                next_pos = list(map(sum, zip(cur_pos, direction)))
                if is_valid(next_pos) and matrix[next_pos[0]][next_pos[1]] > cur_val:
                    all_next_pos.append(next_pos)
                    
            return all_next_pos
        
        def find_longest(matrix, pos, longest_dp):
    
            nonlocal m, n
            row, col = pos
            val = matrix[row][col]
            longest = 1
            
            if longest_dp[row][col] != -1:
                return longest_dp[row][col]
            
            for next_pos in gen_valid_next([row, col], val, matrix):
                longest = max(1 + find_longest(matrix, next_pos, longest_dp), longest)
            
            longest_dp[row][col] = longest
                
            return longest
        
        m = len(matrix)
        n = len(matrix[0])
        longest = 1
        longest_dp = [[-1 for col in range(n)] for row in range(m)]
        for row in range(m):
            for col in range(n):
                if longest_dp[row][col] == -1:
                    longest_dp[row][col] = find_longest(matrix, [row, col], longest_dp)
                longest = max(longest, longest_dp[row][col])

        return longest