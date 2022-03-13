class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        last_occur_idx = {}
        sliding_start_idx = 0
        for idx, ch in enumerate(s):
            cur_char = s[idx]
            
            if cur_char in last_occur_idx and last_occur_idx[cur_char] >= sliding_start_idx:
                max_length = max(max_length, idx - sliding_start_idx)
                sliding_start_idx = last_occur_idx[cur_char] + 1
            else:
                max_length = max(max_length, idx - sliding_start_idx + 1)
            
            last_occur_idx[cur_char] = idx       
            
        return max_length
        