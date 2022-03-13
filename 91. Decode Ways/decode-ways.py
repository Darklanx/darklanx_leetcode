'''
Observations:
    1. We can group 2 digits, but never 3.
    2. If there's a 0 in s at s[i], it must be grouped with s[i-1]. (if s[i-1] is also 0, then it's an invalid s)
    3. Because of (2), we can actually remove s[i-1] and s[i] since it does not affect the solution.
    4. Because of (1), "1234" can be found by all combination of "123" + single "4" 
        and all combination of "12" + "34" (if "34" is valid, which is not in this case)
# 1 -> 1
# 12 -> 1 2, 12
# 123 -> 1 2 3, 1 23, 12 3
# 1234 -> 1 2 3 4, 1 23 4, 12 3 4, (12 34), (1 2 34), 
so if we let `n_decode[i] = numbers of way to decode s[0:i]`
then `n_decode[i] = n_decode[i-1] + is_valid(s[i-1] + s[i]) * n_decode[i-2]`
'''
from typing import List, Deque
from collections import deque
class Solution:
    def numDecodings(self, s: str) -> int:
        NO_GROUP_CH = 'N'
        def remove_zeros(s_deq: Deque):
            new_deq = deque()
            idx = len(s_deq) - 1
            while idx >= 0:
                ch = s_deq[idx]
                if ch == '0':                    
                    if s_deq[idx - 1] == '0' or int(s_deq[idx - 1]) >= 3: 
                        # invalid zero detected
                        return None
                    # 'X0' will be grouped, and since it does not affect the solution,
                    # we don't add it to the deq, but we need to add a NO_GROUP_CH
                    # to avoid invalid group,
                    # ex: "1 10 3" will not be seen as "13" which can be grouped 
                    new_deq.appendleft(NO_GROUP_CH)
                    idx -= 2
                    continue
                    
                new_deq.appendleft(ch)
                idx -= 1
            return new_deq
        
        def is_groupable(ch1, ch2):
            if ch1 == NO_GROUP_CH or ch2 == NO_GROUP_CH:
                return False
    
            if int(ch1 + ch2) > 26:
                return False
            
            return True
            
            
        s_deq = deque(s)
        if s_deq[0] == '0':
            return 0
        s_deq = remove_zeros(s_deq)
        if s_deq is None:
            return 0
                   
        n_decode = [0 for i in range(len(s_deq) + 1)]
        n_decode[0] = 1 # dummy num, define s = "" to have 1 decode
        for idx in range(0, len(s_deq)):
            n_dec_idx = idx + 1
            n_decode[n_dec_idx] = n_decode[n_dec_idx - 1]
            if idx >= 1 and is_groupable(s_deq[idx - 1], s_deq[idx]):
                n_decode[n_dec_idx] += n_decode[n_dec_idx - 2]

        return n_decode[-1]
        
# test cases:
# s = "12" => 2
# s = "102" => "N2" => 1
# s = "01" => 0
# s = "1002" => 0
# s = "10302" => 0
# s = "80102" => 0
# s = "226" => "2 2 6" "22 6", "2 26"


        