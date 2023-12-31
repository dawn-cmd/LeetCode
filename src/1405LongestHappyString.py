import heapq

class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        num = [['a', a], ['b', b], ['c', c]]
        while True:
            num = [x for x in num if x[1]]
            if not num:
                break
            num.sort(key=lambda x: -x[1])
            if len(ans) < 2:
                ans.append(num[0][0])
                num[0][1] -= 1
            elif ans[-1] == ans[-2] == num[0][0]:
                if len(num) == 1:
                    break
                else:
                    ans.append(num[1][0])
                    num[1][1] -= 1
            else:
                ans.append(num[0][0])
                num[0][1] -= 1
        return ''.join(ans)

def main():
    print(Solution().longestDiverseString(a = 7, b = 1, c = 0))
            
if __name__ == "__main__":
    main()