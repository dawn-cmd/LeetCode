from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [0]
        heights = [0] + heights + [0]
        ans = 0
        for i, h in enumerate(heights):
            while h < heights[st[-1]]:
                area = heights[st[-1]] * (i - st[-2] - 1)
                ans = area if area > ans else ans
                st.pop()
            st.append(i)
        return ans
        

print(Solution().largestRectangleArea(heights = [2, 1, 2]))
