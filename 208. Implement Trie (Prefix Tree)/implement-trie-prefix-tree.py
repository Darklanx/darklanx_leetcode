from typing import List
class Node:
    
    def __init__(self, char: str, isEndofWord: bool):
        self.char = char
        self.isEndofWord = isEndofWord
        self.childrens = {}
        
        
class Trie:

    def __init__(self):
        self.char_list = [chr(ch_int) for ch_int in range(ord('a'), ord('z')+1)]
        self.root = Node(None, True)

    def insert(self, word: str) -> None:
        cur_node = self.root

        for ch_idx, ch in enumerate(word):
            next_node = self._get_node_with_ch(cur_node, ch)
            if next_node is None:

                cur_node.childrens[ch] = Node(ch, False)
                next_node = cur_node.childrens[ch]
            cur_node = next_node
        cur_node.isEndofWord = True
            
    def search(self, word: str) -> bool:
        last_node = self._get_last_node_start_with(word)
        if last_node is None or last_node.isEndofWord == False:
            return False
        else:
            return True
    
    @staticmethod
    def _get_node_with_ch(cur_node: Node, ch: str):
        if ch in cur_node.childrens:
            return cur_node.childrens[ch]
        else:
            return None
    
    def _get_last_node_start_with(self, prefix: str):
        cur_node = self.root
        search_idx = 0
        while(search_idx != len(prefix)):
            next_node = self._get_node_with_ch(cur_node, prefix[search_idx])
            if next_node is None:
                return None
            cur_node = next_node
            search_idx += 1   
        
        if cur_node == self.root:
            return None
        else:
            return cur_node

    def startsWith(self, prefix: str) -> bool:
        return self._get_last_node_start_with(prefix) is not None

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)