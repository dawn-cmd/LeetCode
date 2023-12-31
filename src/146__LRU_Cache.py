class LRUCache:

    def __init__(self, capacity: int):
        self.st = [-1 for _ in range(capacity)]

    def get(self, key: int) -> int:
        return self.st[key]

    def put(self, key: int, value: int) -> None:
        self.st[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
