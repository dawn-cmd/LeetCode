from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, now, layer):
        if now == None:
            return True
        if layer % 2 == 0 and now.val % 2 == 0:
            return False
        elif layer % 2 == 1 and now.val % 2 == 1:
            return False
        if len(self.layer_num) == layer:
            self.layer_num.append(now.val)
        elif layer % 2 == 1 and self.layer_num[layer] <= now.val:
            return False
        elif layer % 2 == 0 and self.layer_num[layer] >= now.val:
            return False
        else:
            self.layer_num[layer] = now.val
        return self.dfs(now.left, layer + 1) and self.dfs(now.right, layer + 1)

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.layer_num = []
        return self.dfs(root, 0)

def main():
    treenode = TreeNode(1)
    solution = Solution()
    print(solution.isEvenOddTree(treenode))

if __name__ == "__main__":
    main()