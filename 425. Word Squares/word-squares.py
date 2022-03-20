'''
"ball","area","lead","lady"

"ball"
"area"
"lead"
"lady"

prefix-tree?
'''
class Node:
    def __init__(self, ch=None):
        self.ch = ch
        self.children = {}
        self.is_EOW = False
        
class PrefixTree:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.add_word(word)
    
    def get_words_with_prefix(self, prefix):
        def get_all_suffixes(node):
            if len(node.children) == 0:
                return [""]
            all_suffixes = []
            for new_ch, child in node.children.items():
                all_suffixes.extend([new_ch + suf for suf in get_all_suffixes(child)])
            return all_suffixes
            
        cur_node = self.root
        for ch in prefix:
            if ch not in cur_node.children:
                return []
            cur_node = cur_node.children[ch]
        
        suffixes = get_all_suffixes(cur_node)

        return [prefix + suf for suf in suffixes]
        
    def add_word(self, word):
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = Node(ch)
                
            cur_node = cur_node.children[ch] 
            
        cur_node.is_EOW = True
    
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def build_word_squares(cur_words, length, trie) -> List[List[str]]:
            if length == len(cur_words):

                return [cur_words]

            cur_word_idx = len(cur_words)
            all_word_squares = []
            prefix = "".join([word[cur_word_idx] for word in cur_words])

            for word in trie.get_words_with_prefix(prefix):
                all_word_squares.extend(build_word_squares(cur_words + [word], length, trie))
            return all_word_squares
            
        trie = PrefixTree(words)

        all_word_squares = []
        l = len(words[0])
        for word in words:
            all_word_squares.extend(build_word_squares([word], length=l, trie=trie))

        return all_word_squares
            
            
        
        