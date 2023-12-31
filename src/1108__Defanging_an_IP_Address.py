class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

print(Solution().defangIPaddr("255.100.50.0"))
