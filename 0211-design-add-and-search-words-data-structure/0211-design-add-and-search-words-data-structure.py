class Trie:
    def __init__(self):
        self.children={}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root =  Trie()

    def addWord(self, word: str) -> None:

        curr_node= self.root

        for char in word:
            if char not in curr_node.children:
                new_node= Trie()
                curr_node.children[char] = new_node
                curr_node= new_node
            else:
                curr_node= curr_node.children[char]
        curr_node.endWord= True
        

    def search(self, word: str) -> bool:

        n= len(word)
        def helper(index, curr_node):
            if index==n and curr_node.endWord:
                return True
            if index==n:
                return False
            
            if word[index]!='.':

                if word[index] not in curr_node.children:
                    return False
                else:
                    return helper(index+1, curr_node.children[word[index]])
            
            else:
                for key,value in curr_node.children.items():
                    if helper(index+1, value):
                        return True
            return False
        return helper(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)