class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    def find_prefix(self, prefix: str):
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur
    
    def autocomplete(self, prefix: str):
        results = []
        prefix_node = self.find_prefix(prefix)
        if not prefix_node:
            return results
        self._dfs(prefix_node, prefix, results)
        return results
    
    def _dfs(self, node, prefix, results):
        if node.end_of_word:
            results.append(prefix)
        for char, child, in node.children.items():
            self._dfs(child, prefix + char, results)
    
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("orange")
    print(trie.search("orange"))
    print(trie.search("oran"))
    print(trie.starts_with("ora"))
    trie.insert("banana")
    print(trie.starts_with("b"))
    print(trie.starts_with("ba"))