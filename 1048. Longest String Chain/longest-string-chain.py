'''
find predecessors => O(l^2), called n times => O(n * l^2)
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def find_pred(w, words_with_l):
            if len(w) <= 1:
                return []
            l = len(w)
            preds = []
            for i in range(l):
                pred = w[0:i] + w[i+1:]
                if pred in words_with_l[l-1]:
                    preds.append(pred)
            return preds
                 
        len_chain = dict([(w, 1) for w in words]) # length of reversed chain
        next_chain = defaultdict(lambda : None)
        words_with_l = defaultdict(list)
        max_l = 0
        best_l = 1
        for w in words:
            words_with_l[len(w)].append(w)
            max_l = max(max_l, len(w))
            
        # first two for loop => O(n)
        for l in range(max_l, 0, -1):  
            for w in words_with_l[l]:
                
                preds = find_pred(w, words_with_l) # O(l^2)
                for pred in preds: # O(l)
                    if len_chain[w] + 1 > len_chain[pred]:
                        len_chain[pred] = len_chain[w] + 1
                        next_chain[pred] = w
                        best_l = max(len_chain[pred], best_l)
        # O(n * (l^2+l)) = O(n * l^2)
        return best_l 
                        
                    
                
                
            