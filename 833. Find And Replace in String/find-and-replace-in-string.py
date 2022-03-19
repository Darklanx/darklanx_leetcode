class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        new_str_list = []
        ops = sorted([op for op in zip(indices, sources, targets)])
        next_valid = 0
        op_idx = 0
        for i, ch in enumerate(s):
            if i < next_valid:
                continue
            
            if op_idx >= len(ops):
                # no more operation, just append
                new_str_list.append(s[i:])
                break
        
            idx, src, target = ops[op_idx]
            len_src = len(src)
            replaced = False
            if i == idx:
                if s[idx:idx+len_src] == src:
                    new_str_list.append(target)
                    next_valid = idx + len_src 
                    replaced = True
                    if next_valid > len(s):
                        break
                op_idx += 1
                
            if not replaced:
                new_str_list.append(ch)
                  
        return "".join(new_str_list)