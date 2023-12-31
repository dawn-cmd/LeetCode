from sympy import li


class Solution:
    
    def pushDominoes(self, dominoes: str) -> str:
        s = list(dominoes)
        s = ['L'] + s + ['R']
        i = 1
        while i < len(s) - 1:
            if s[i] == '.':
                j = i
                while s[j + 1] == '.':
                    j += 1
                if s[i - 1] == s[j + 1]:
                    s[i:j + 1] = [s[i - 1] for k in range(j - i + 1)]
                elif s[i - 1] == 'R' and s[j + 1] == 'L':
                    if (i + j) % 2 == 0:
                        mid = (i + j) // 2
                        s[i:mid] = [s[i - 1] for k in range(mid - 1 - i + 1)]
                        s[mid + 1:j + 1] = [s[j + 1] for k in range(j - mid)]
                    else:
                        mid = (i + j) // 2
                        s[i:mid + 1] = [s[i - 1] for k in range(mid - i + 1)]
                        s[mid + 1:j + 1] = [s[j + 1] for k in range(j - mid)]
                i = j + 1
            else:
                i += 1
        return ''.join(s[1:-1])

def main():
    print(Solution().pushDominoes(dominoes = ".L.R...LR..L.."))

if __name__ == "__main__":
    main()
