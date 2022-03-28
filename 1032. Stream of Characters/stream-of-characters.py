class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
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
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)