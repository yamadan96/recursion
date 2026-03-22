def middleSubstring(stringInput):
    n = len(stringInput)
    if n <= 2:
        return stringInput[0]
    middle = n // 2
    start = (middle + 1) // 2
    return stringInput[start:start + middle]


# テスト
print(middleSubstring("A"))         # A
print(middleSubstring("AB"))        # A
print(middleSubstring("ABCDE"))     # BC
print(middleSubstring("ABCDEF"))    # CDE
print(middleSubstring("ABCDEFG"))   # CDE
print(middleSubstring("ABCDEFGH"))  # CDEF
