class Trie:

    class node:

        def __init__(self) -> None:
            self.isEnd = False
            self.next = [None for _ in range(26)]

    def __init__(self):
        self.root = self.node()        

    def insert(self, word: str) -> None:
        now = self.root
        i = 0
        while i < len(word):
            id = ord(word[i]) - ord('a')
            if now.next[id] == None:
                now.next[id] = self.node()
            now = now.next[id]
            i += 1
        now.isEnd = True

    def search(self, word: str) -> bool:
        now = self.root
        i = 0
        while i < len(word):
            id = ord(word[i]) - ord('a')
            if now.next[id] == None:
                return False
            now = now.next[id]
            i += 1
        return now.isEnd

    def startsWith(self, prefix: str) -> bool:
        now = self.root
        i = 0
        while i < len(prefix):
            id = ord(prefix[i]) - ord('a')
            if now.next[id] == None:
                return False
            now = now.next[id]
            i += 1
        return True
