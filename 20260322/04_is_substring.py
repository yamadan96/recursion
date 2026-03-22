def isSubstring(s1, s2):
    return s2 in s1


# テスト
print(isSubstring("hello world!", "world!"))   # True
print(isSubstring("hello world!", "World!"))   # False
print(isSubstring("hello pluto!", "world!"))   # False
print(isSubstring("hello world!", "d!rolw"))   # False
print(isSubstring("hello pluto!", "do"))       # False
print(isSubstring("Fly away duck.", "aw"))     # True
