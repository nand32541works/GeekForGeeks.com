class Trie:
    def __init__(self):
        self.alphas = [None] * 26
        self.end = False
    def insert(self, word: str):
        node = self
        for ch in word:
            c = ord(ch) - ord('a')
            if node.alphas[c] == None:
                node.alphas[c] = Trie()
            node = node.alphas[c]
        node.end = True
    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            c = ord(ch) - ord('a')
            if node == None:
                return False
            node = node.alphas[c]
        return node and node.end
    def isPrefix(self, word: str) -> bool:
        node = self
        for ch in word:
            if node == None:
                return False
            c = ord(ch) - ord('a')
            node = node.alphas[c]
        return node != None
