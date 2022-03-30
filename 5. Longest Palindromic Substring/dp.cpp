#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n));
        int max_l = 0, max_r = 0;
        for(int i = n-1; i >= 0; i--){
            for(int j = n-1; j >= i; j--){
                if(s[i] != s[j]){
                    dp[i][j] = false;
                    
                }else{
                    if (i+1 >= j-1){
                        dp[i][j] = true;
                    }else{
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                if(dp[i][j]){
                    if (j-i+1 > max_r-max_l+1){
                        max_r = j;
                        max_l = i;
                    }
                }
                
            }      
        }
        return s.substr(max_l, max_r-max_l+1);
    }
};