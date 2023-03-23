from tkinter import SOLID


class Solution:
    
    def convertToBase7(self, num: int) -> str:
        ans = ""
        negative = False
        if num < 0:
            negative = True
            num *= -1
        while num >= 7:
            ans = str(num % 7) + ans
            num //= 7
        ans = str(num) + ans
        if negative:
            ans = '-' + ans
        return ans

def main():
    print(Solution().convertToBase7(-7))

if __name__ == "__main__":
    main()