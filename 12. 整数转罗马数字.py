class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 4: "IV", 5: 'V', 9: "IX", 10: 'X', 40: "XL", 50: 'L', 90: "XC", 100: 'C', 400: "CD", 500: 'D', 900: "CM", 1000: "M"}
        ans = ''
        for unit in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while num >= unit:
                ans += d[unit]
                num -= unit
        return ans

def main():
    print(Solution().intToRoman(num = 2147))

if __name__ == "__main__":
    main()
