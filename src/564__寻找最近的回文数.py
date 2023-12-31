from sys import maxsize


class Solution:
    
    def nearestPalindromic(self, n: str) -> str:
        planA = n[:(len(n) // 2 if len(n) % 2 == 0 else len(n) // 2 + 1)]
        planB = str(int(planA) - 1) + ('' if len(n) % 2 == 1 else '#')
        planC = str(int(planA) + 1) + ('' if len(n) % 2 == 1 else '#')
        planA += '' if len(n) % 2 == 1 else '#'

        def bulid(s: str) -> str:
            s += s[-2::-1]
            return s.replace('#', '')
        
        planA = int(bulid(planA))
        planB = int(bulid(planB))
        planC = int(bulid(planC))
        planE = pow(10, len(n)) + 1
        planD = pow(10, len(n) - 1) - 1
        min_dif = maxsize
        ans = -1
        n = int(n)
        for num in [planA, planB, planC, planD, planE]:
            if abs(num - n) < min_dif and num - n != 0:
                min_dif = abs(num - n)
                ans = num
            elif abs(num - n) == min_dif and ans > num:
                ans = num
        return str(ans)
    
def main():
    print(Solution().nearestPalindromic(n = "1213"))

if __name__ == "__main__":
    main()
    

