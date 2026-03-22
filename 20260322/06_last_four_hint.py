def lastFourHint(stringInput):
    if len(stringInput) < 6:
        return "There is no Hint"
    return "Hint is:" + stringInput[-4:]


# テスト
print(lastFourHint("text"))             # There is no Hint
print(lastFourHint("Ocean"))            # There is no Hint
print(lastFourHint("the ocean is blue")) # Hint is:blue
print(lastFourHint("abcdef"))           # Hint is:cdef
print(lastFourHint("integer"))          # Hint is:eger
print(lastFourHint("1-545-452-5123"))   # Hint is:5123
