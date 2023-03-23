from typing import List


class Solution:
    
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        max_nums = set()
        for i in range(len(matrix[0])):
            max_nums.add(max([x[i] for x in matrix]))
        return [min(x) for x in matrix if min(x) in max_nums]
    
def main():
    print(Solution().luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))

if __name__ == "__main__":
    main()