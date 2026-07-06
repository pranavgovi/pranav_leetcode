class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node= self.root
        for char in word:
            if char not in curr_node.children:
                new_node= TrieNode()
                curr_node.children[char] = new_node
                curr_node= new_node
            else:
                curr_node = curr_node.children[char]
        curr_node.endWord= True    
        

        

    def search(self, word: str) -> bool:
        curr_node= self.root
        for char in word:
            if char not in curr_node.children:
                return False
            else:
                curr_node=  curr_node.children[char]
        if not curr_node.endWord:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr_node= self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            else:
                curr_node=  curr_node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)