from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_def = 0
        for character in properties:
            if max_def > character[1]:
                ans += 1
            else:
                max_def = character[1]
        return ans

def main():
    solution = Solution()
    print(solution.numberOfWeakCharacters(properties = [[10,1],[5,1],[7,10],[4,1],[5,9],[6,9],[7,2],[1,10]]))

if __name__ == "__main__":
    main()