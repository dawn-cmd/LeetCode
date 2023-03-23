from typing import List

class Solution:
    
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        id = 0
        while id < len(bits):
            if id == len(bits) - 1:
                return True if bits[id] == 0 else False
            if bits[id] == 0:
                id += 1
            else:
                id += 2
        return False

def main():
    print(Solution().isOneBitCharacter(bits = [1, 1, 1, 0]))

if __name__ == "__main__":
    main()