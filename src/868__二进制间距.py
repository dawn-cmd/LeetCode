class Solution:
    def binaryGap(self, n: int) -> int:
        num = bin(n)
        ans = 0
        id = num.find('1')
        pre = id
        for i in range(id + 1, len(num)):
            if num[i] == '1':
                ans = max(ans, i - pre)
                pre = i
        return ans

def main():
    print(Solution().binaryGap(n = 22))
            
if __name__ == "__main__":
    main()
