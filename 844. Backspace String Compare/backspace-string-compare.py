class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s, s_idx):
            '''
            return the index of valid character in s (reverse order)
            '''
            if s_idx < 0:
                return -1
            removing = 0
            while s_idx >= 0:
                if s[s_idx] == '#':
                    removing += 1
                else:
                    if removing == 0:
                        return s_idx
                    else:
                        # skip this
                        removing -= 1
                        
                s_idx -= 1
            return -1
            
        s_idx = len(s) - 1
        t_idx = len(t) - 1
        while s_idx >= 0 or t_idx >= 0:
            s_idx = process(s, s_idx)
            t_idx = process(t, t_idx)
            if t_idx < 0 and s_idx < 0:
                return True
            
            if t_idx >= 0 and s_idx >= 0:
                if s[s_idx] != t[t_idx]:
                    return False
            else:
                return False
            s_idx -= 1
            t_idx -= 1
        return True
        