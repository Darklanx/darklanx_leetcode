 
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(count_s_ch, count_t_ch):
            for ch, count in count_t_ch.items():
                if count_s_ch[ch] < count_t_ch[ch]:
                    return False
            return True
        
        if len(s) == 0 or len(t) == 0:
            return ""
        
        l = 0
        r = len(s) - 1
        count_s_ch, count_t_ch = Counter(s), Counter(t)

        if not is_valid(count_s_ch, count_t_ch):
            return ""
        
        # find minimal set s[l:r+1] that satisfy condition
        while r >= l:
            ch = s[r]
            if count_s_ch[ch] - 1 >= count_t_ch[ch]:
                count_s_ch[ch] = count_s_ch[ch] - 1
                r -= 1
            else:
                break

        min_idx = [l, r]
        min_len = r - l + 1
        while r < len(s):
            # remove from left until minimized
            while l < r:
                ch = s[l]
                if count_s_ch[ch] - 1 >= count_t_ch[ch]:
                    l += 1
                    count_s_ch[ch] -= 1
                else:
                    break

            # update new min_len
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_idx = [l, r]
            
            # make s[l, r+1] invalid by removing the leftmost char
            missing_char = s[l]
            l += 1
            count_s_ch[missing_char] = count_s_ch[missing_char] - 1
            
        
            # increasing window from rhs until valid, 
            r += 1
            while r < len(s): 
                count_s_ch[s[r]] += 1
                if s[r] == missing_char:
                    break
                r += 1
                
            # At this point, if r == len(s), 
            # then we have failed to find a valid r in the previous step
            
        return s[min_idx[0] : min_idx[1]+1]
        
        