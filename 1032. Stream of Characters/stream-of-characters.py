class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.nodes = []
        self.reverse_stream = deque()
        for w in words:
            cur = self.trie
            for ch in reversed(w):
                if ch not in cur:
                    cur[ch] = dict()
                cur = cur[ch]
            cur['$'] = True


                        
    def query(self, letter: str) -> bool:
        self.reverse_stream.appendleft(letter)
        cur = self.trie
        for ch in self.reverse_stream:
            if ch not in cur:
                return False
            if '$' in cur[ch]:
                return True
            cur = cur[ch]
            
        return False
            
#         new_nodes = []
#         found = False
        
#         for node in self.nodes:
#             if letter in node:
#                 new_nodes.append(node[letter])
#                 if '$' in node[letter]:
#                     found = True
        
#         if letter in self.trie:
#             new_nodes.append(self.trie[letter])
#             if '$' in self.trie[letter]:
#                 found = True
#         self.nodes = new_nodes
#         return found
                
'''
cd f kl
a
'''   
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)