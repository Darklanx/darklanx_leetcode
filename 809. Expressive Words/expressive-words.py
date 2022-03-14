'''
edge cases:
empty:
""

single:
"a"

repeated char:
"abaab"

long unique:
"aaaaaa"
'''
from typing import List
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def group_str(s: str) -> List: # "aab"
            if len(s) == 0:
                return []
            group_list = []
            count = 1
            cur_ch = s[0]
            idx = 1
            while idx < len(s):
                if s[idx] == cur_ch:
                    count += 1
                else:
                    group_list.append(cur_ch * count)
                    count = 1
                    cur_ch = s[idx]
                idx += 1
            group_list.append(cur_ch * count)
            
            return group_list
        
        def is_stretchable(word_groups: List, target_groups: List) -> bool:
            if len(word_groups) != len(target_groups):
                return False
            
            for i in range(len(word_groups)):
                g1 = word_groups[i]
                target_g = target_groups[i]

                if g1[0] != target_g[0]: 
                    # if not same character
                    return False
                if len(target_g) < len(g1):
                    # g1 is longer than target_g (can't stretch)
                    return False
                if len(target_g) < 3 and len(target_g) != len(g1):
                    # different len while unstetchable
                    return False
            return True
                    
                  
        n_count = 0
        s_groups = group_str(s)
        for word in words:
            word_groups = group_str(word)
            if is_stretchable(word_groups, s_groups):
                n_count +=1
        
        return n_count

                    
            
                
        