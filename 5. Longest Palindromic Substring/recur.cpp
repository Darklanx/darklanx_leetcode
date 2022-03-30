#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    bool is_palin(string& s, int l, int r, vector<vector<int>>& dp){
        if (l >= r)
            return true;
        
        if (dp[l][r] == -1){
            if (s[l] != s[r])
                return false;
            dp[l][r] = is_palin(s, l+1, r-1, dp);
            
        }
        return dp[l][r];
        
    }

    string longestPalindrome(string s) {
        int max_l = 0, max_r = 0;
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        for(int l=0; l<n; l++){
            for(int r=l; r<n; r++){
                if (is_palin(s, l, r, dp)){
                    if (r-l+1 > max_r-max_l+1){
                        max_l = l;
                        max_r = r;
                    }
                }
            }
        }
        return s.substr(max_l, max_r-max_l+1);
    }
    

};