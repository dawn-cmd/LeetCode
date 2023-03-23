from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timePoints.append(str(int(timePoints[0][:2]) + 24) + timePoints[0][-3:])

        def minus(st: str, ed: str) -> int:
            return (int(ed[:2]) - int(st[:2])) * 60 + int(ed[-2:]) - int(st[-2:])

        return min([minus(st=timePoints[i], ed=timePoints[i + 1]) for i in range(len(timePoints) - 1)])

def main():
    solution = Solution()
    print(solution.findMinDifference(["23:59","00:00"]))

if __name__ == "__main__":
    main()