import random


class SkipListNode:
    __slots__ = 'forward', 'val'

    def __init__(self, val: int, level: int) -> None:
        self.val = val
        self.forward = [None] * level

class Skiplist:
    # skiplist has a structure like this
    # lv0      -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->  
    # lv1 -inf ------> 2 -> 3 -----------> 6 -> None
    # lv2      -----------> 3 ----------------> 

    def __init__(self):
        self.maxLevel = 32
        self.pRate = 0.5  # the probability one node in layer[n] also exist in layer[n + 1]
        self.head = SkipListNode(float('-inf'), self.maxLevel)
    
    # define the depth of node when you add it in skiplist
    def randomLevel(self) -> int:
        ans = 1
        while ans <= self.maxLevel and random.random() < self.pRate:
            ans += 1
        return ans

    def search(self, target: int) -> bool:
        now = self.head
        # find the most close node which smaller than target in each layer
        for i in range(self.maxLevel - 1, -1, -1):
            while now.forward[i] and now.forward[i].val < target:
                now = now.forward[i]
        # node now is the most close one to the target, so now.forward[0] should be target
        now = now.forward[0]
        return now is not None and now.val == target

    def add(self, num: int) -> None:
        update = [None] * self.maxLevel  # update info for each level
        now = self.head
        for i in range(self.maxLevel - 1, -1, -1):
            while now.forward[i] and now.forward[i].val < num:
                now = now.forward[i]
            update[i] = now
        level = self.randomLevel()
        newNode = SkipListNode(num, level)
        # add newNode to update[i]
        for i in range(level):
            newNode.forward[i] = update[i].forward[i]
            update[i].forward[i] = newNode

    def erase(self, num: int) -> bool:
        update = [None] * self.maxLevel
        now = self.head
        for i in range(self.maxLevel - 1, -1, -1):
            while now.forward[i] and now.forward[i].val < num:
                now = now.forward[i]
            update[i] = now
        now = now.forward[0]
        if now is None or now.val != num:
            return False
        for i in range(self.maxLevel):
            if update[i].forward[i] != now:
                break
            update[i].forward[i] = now.forward[i]
        return True
