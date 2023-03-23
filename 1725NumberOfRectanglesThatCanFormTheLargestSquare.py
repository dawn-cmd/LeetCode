from typing import List


class Solution:

    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        rectangles = [min(x) for x in rectangles]
        return rectangles.count(max(rectangles))

def main():
    print(Solution().countGoodRectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]]))

if __name__ == "__main__":
    main()