class Solution:
    def numSplits(self, s: str) -> int:
        l_set, r_set = set(), set()
        l_count, r_count = [0 for i in range(len(s))], [0 for i in range(len(s))]
        l_counter, r_counter = 0, 0
        for l_idx, r_idx in zip(range(len(s)), reversed(range(len(s)))):
            if s[l_idx] not in l_set:
                l_counter += 1    
                l_set.add(s[l_idx])
            l_count[l_idx] = l_counter   
            
            if s[r_idx] not in r_set:
                r_counter += 1 
                r_set.add(s[r_idx])
            r_count[r_idx] = r_counter
            
        n_splits = 0
        for idx in range(len(s) - 1):
            if l_count[idx] == r_count[idx+1]:
                n_splits += 1
            
        return n_splits