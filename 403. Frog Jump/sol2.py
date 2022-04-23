class Solution:
    def canCross(self, stones: List[int]) -> bool:
        arrive_k = defaultdict(set) # key: pos, value: set of possible k arrive at pos
        arrive_k[stones[0]].add(0)
        for st in stones:
            for pos_k in arrive_k[st]:
                next_k = [pos_k-1, pos_k, pos_k+1]
                for k in next_k:
                    if k <= 0:
                        continue
                    arrive_k[st + k].add(k)
        
        return len(arrive_k[stones[-1]]) > 0 