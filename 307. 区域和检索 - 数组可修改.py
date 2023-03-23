from typing import List


class NumArray:
    def lowbit(self, id: int) -> int:
        return id & (-id)

    def __init__(self, nums: List[int]):
        self.a = [0 for _ in range(len(nums) + 1)]
        self.c = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, index: int, val: int) -> None:
        index += 1
        dif = val - self.a[index]
        self.a[index] = val
        while index < len(self.c):
            self.c[index] += dif
            index += self.lowbit(index)

    def sumRange(self, left: int, right: int) -> int:
        ansl, ansr = 0, 0
        right += 1
        while left > 0:
            ansl += self.c[left]
            left -= self.lowbit(left)
        while right > 0:
            ansr += self.c[right]
            right -= self.lowbit(right)
        return ansr - ansl


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
