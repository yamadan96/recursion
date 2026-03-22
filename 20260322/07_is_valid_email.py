def isValidEmail(email):
    if email.startswith("@"):
        return False
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    after_at = email.split("@")[1]
    if "." not in after_at:
        return False
    return True


# テスト
print(isValidEmail("ccc@aaa.com"))    # True
print(isValidEmail("c@cc@aaa.com"))   # False
print(isValidEmail("cc c@aaa.com"))   # False
print(isValidEmail("cc.c@aaacom"))    # False
