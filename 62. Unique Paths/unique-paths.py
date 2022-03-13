# 28 21 15 10 6 3 1  
# 7  6  5  4  3 2 1
# 1  1  1  1  1 1 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def get_another_row(row_num):
            return (row_num + 1) % 2
        
        current_row = 0
        dp = [[0 for i in range(n)] for i in range(2)]
        for j in range(n):
            dp[current_row][j] = 1
        current_row = get_another_row(current_row)
        m -= 1

        while m > 0:
            for j in reversed(range(n)):
                another_row = get_another_row(current_row)
                dp[current_row][j] = 0
                dp[current_row][j] += dp[another_row][j]
                if j + 1 < n:
                    dp[current_row][j] += dp[current_row][j + 1]

            
            current_row = get_another_row(current_row)
            m -= 1
        return dp[get_another_row(current_row)][0]

            
        