class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string= str(bin(n))[2:]
        remaining = 32 - len(binary_string)
        binary_string = ("0" * remaining) + binary_string
        reversed_binary = "".join(reversed(binary_string))
        res= int(reversed_binary, 2)
        return res