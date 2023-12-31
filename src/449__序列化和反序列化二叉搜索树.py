# Definition for a binary tree node.
from typing import Type


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        # Encodes a tree to a single string.
        if root == None:
            return ""
        return ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        

    def deserialize(self, data: str) -> TreeNode:
        nums = list(map(int, data.split()))
        if nums == []:
            return None
        ans = TreeNode(nums[0])
        tmp = [str(num) for num in nums[1:] if num < ans.val]
        if tmp:
            ans.left = self.deserialize(' '.join(tmp))
        tmp = [str(num) for num in nums[1:] if num > ans.val]
        if tmp:
            ans.right = self.deserialize(' '.join(tmp))
        return ans
        # Decodes your encoded data to tree.
        
def main():
    print(Codec().serialize(Codec().deserialize("2 1 3")))

if __name__ == "__main__":
    main()
