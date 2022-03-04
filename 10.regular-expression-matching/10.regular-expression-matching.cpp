// struct Pattern{
//     char ch;
//     bool starred = false;  
    
// };

// vector<Pattern> minimizePattern(vector<Pattern> &pattern){
//     vector<Pattern> min_pattern;
//     for(int i = 0; i < pattern.size(); ){
//         if(pattern[i].starred == false){
//             min_pattern.push_back(pattern[i]);
//             i++;
//         }
//         else{ // starred
//             if(pattern[i].ch == '.'){
//                 min_pattern.push_back(pattern[i]);
//                 while(pattern[i].starred){
//                     i++;
//                     if(i == pattern.size()){
//                         break;
//                     }
//                 }
//             }else{
//                 min_pattern.push_back(pattern[i]);
//                 while(pattern[i].starred && pattern[i].ch == min_pattern.back().ch){
//                     i++;
//                     if(i == pattern.size()){
//                         break;
//                     }
//                 }
//             }
//         }
//     }
//     return min_pattern;
// }
// vector<Pattern> strToPattern(string &p){
//     vector<Pattern> pattern;
//     for(int i = 0; i < p.size(); i++){
//         if(p[i] == '*'){
//             continue;
//         }
//         if(i+1 < p.size() and p[i+1] == '*'){
//             pattern.push_back(Pattern{.ch=p[i], .starred=true});                             
//         }
//         else{
//             pattern.push_back(Pattern{.ch=p[i], .starred=false});
//         }
        
//     }
//     return minimizePattern(pattern);
    
// }

// string patternToString(vector<Pattern>& pattern){
//     string p ="";
//     for(int i=0; i < pattern.size(); i++){
//         p += pattern[i].ch;
//         if (pattern[i].starred)
//             p += '*';
//     }
//     return p;
// }
// bool isPossibleLength(string &s, vector<Pattern>& pattern){
//     int pattern_min_l = 0;
//     for(int p_i = 0; p_i < pattern.size(); p_i++){
//         if(pattern[p_i].starred == false){
//             pattern_min_l += 1;
//         }
//     }
//     if(s.size() < pattern_min_l){
//         return false;
//     }
//     return true;
// }

// int countConsecutiveChar(string &s, int start, char &ch){
//     int n = 0;
//     int i = start;
//     if(ch == '.')
//         return s.size() - start;
//     while(i < s.size() && s[i] == ch){
//         n++;
//         i++;
//     }
//     return n;
    
// }
// class Solution {
// public:
//     bool isMatch(string s, string p) {
//         vector<Pattern> pattern = strToPattern(p);
//         if(!isPossibleLength(s, pattern)){ // check if p is too long to fit s
//             return false;
//         }
//         if( s.size() > 0 && pattern.size() ==0){
//             return false;
//         }
//         if(s.size() == 0 && pattern.size() == 0){
//             return true;
//         }else{
//             cout << "s: " << s << endl;
//             cout << "p: " << p << endl;
//         }
        
//         int matching_index = 0;
//         for(int p_i = 0; p_i < pattern.size(); p_i++){
//             Pattern *cur_p = &pattern[p_i];
//             // if not starred, then simply check if it's the same
//             if(cur_p->starred == false){
//                 if(cur_p->ch != '.'){
//                     if(cur_p->ch != s[matching_index]){
//                         return false;
//                     }
//                     matching_index++;
//                 }
//                 else{ // '.'
//                     matching_index++;
//                 }
                
//             }
//             else{ // starred
//                 /*
//                 starred character can represent 0+ character
//                 so we try every possible number of it.

//                 */
//                 int n_consecutive_char = countConsecutiveChar(s, matching_index, cur_p->ch);
//                 // sub_pattern is the pattern without current 
//                 vector<Pattern> sub_pattern;
//                 copy(pattern.begin() + p_i + 1, pattern.end(), back_inserter(sub_pattern));
//                 string str_sub_pattern = patternToString(sub_pattern);
//                 for(int i_count=0; i_count <= n_consecutive_char; i_count++){
//                     if(isMatch(s.substr(matching_index+i_count, string::npos), str_sub_pattern)){
//                         return true;
//                     }      
//                 }      
//                 return false;
//             }      
//         }
//         if(matching_index == s.size())
//             return true;
//         else
//             return false;
//     }
// };


// class Solution {
// public:
//     bool isMatch(string s, string p) {
//         int m = s.size(), n = p.size();
//         vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
//         dp[0][0] = true;
//         for (int i = 0; i <= m; ++i) {
//             for (int j = 1; j <= n; ++j) {
//                 if (j > 1 && p[j - 1] == '*') {
//                     dp[i][j] = dp[i][j - 2] || (i > 0 && (s[i - 1] == p[j - 2] || p[j - 2] == '.') && dp[i - 1][j]);
//                 } else {
//                     dp[i][j] = i > 0 && dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
//                 }
//             }
//         }
//         return dp[m][n];
//     }
// };

class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty()) return s.empty();
        if (p.size() > 1 && p[1] == '*') {
            return isMatch(s, p.substr(2)) || (!s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p));
        } else {
            return !s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1));
        }
    }
};