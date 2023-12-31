from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.replace(' ', '')
        for i in range(10):
            licensePlate = licensePlate.replace(str(i), '')
        licensePlate = licensePlate.lower()
        words.sort(key=lambda i: len(i))
        h = {}
        for i in licensePlate:
            if h.get(i) != None:
                h[i] += 1
            else:
                h[i] = 1
        for i in words:
            tmp = {}
            for j in i:
                if tmp.get(j) != None:
                    tmp[j] += 1
                else:
                    tmp[j] = 1
            is_find = True
            for j in h:
                if tmp.get(j) == None:
                    is_find = False
                    break
                elif tmp[j] < h[j]:
                    is_find = False
                    break
            if is_find == True:
                return i

def main():
    solution = Solution()
    licensePlate = "1s3 456"
    words = ["pest", "looks", "stew", "show"]
    print(solution.shortestCompletingWord(licensePlate, words))

if __name__ == "__main__":
    main()