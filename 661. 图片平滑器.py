from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]

        def pointSmoother(x: int, y: int) -> int:
            s = 0
            cnt = 0
            for i in range(max(0, x - 1), min(len(img), x + 2)):
                for j in range(max(0, y - 1), min(len(img[x]), y + 2)):
                    s += img[i][j]
                    cnt += 1
            return s // cnt

        for i in range(len(img)):
            for j in range(len(img[i])):
                ans[i][j] = pointSmoother(i, j)
        return ans

def main():
    print(Solution().imageSmoother(img = [[100,200,100],[200,50,200],[100,200,100]]))

if __name__ == "__main__":
    main()
