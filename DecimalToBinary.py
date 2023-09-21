"""
write a recursive function that take in integer and return a string of binary number for this number

"""


def decimalToBinary(i: int,s = "") -> str:
    if i == 0:
        return s[::-1]

    s += str(i % 2)
    return decimalToBinary(i//2,s)

def decimalToBinary2(i: int) -> str:

    if i == 0:
        return ""

    return decimalToBinary2(i // 2) + str(i % 2)

print(decimalToBinary(5))
print(decimalToBinary2(5))  # should be "101"
