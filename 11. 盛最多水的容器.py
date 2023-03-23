from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        head = 0
        end = len(height) - 1
        while end - head:
            ans = max(ans, (end - head) * min(height[end], height[head]))
            if height[end] < height[head]:
                end -= 1
            else:
                head += 1
        return ans

def main():
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == "__main__":
    main()
