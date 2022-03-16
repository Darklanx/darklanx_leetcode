'''
BFS
1. insert all word to queue in word list with diff = 1 
2. loop words in queue, insert all word with diff = 1 to queue (avoid dup)
O(n * max_length * n)
'''
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_diff_by_one(w1, w2):
            n_diff = 0
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    n_diff += 1
                    if n_diff > 1:
                        return False
            
            return n_diff == 1
                
                
        deq = deque()
        deq.appendleft((beginWord, 1))
        word_set = set(wordList)
        while len(deq) > 0:
            cur_w, path_len = deq.pop()
            if cur_w == endWord:
                return path_len
            used_set = set()
            for next_word in word_set:
                if is_diff_by_one(cur_w, next_word):
                    deq.appendleft((next_word, path_len + 1))
                    used_set.add(next_word)
                    
            word_set = word_set - used_set
                
        return 0
            
            
        
        