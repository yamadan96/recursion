def insertUnderscoreAt(s, i):
    if i >= len(s):
        return s
    return s[:i] + "_" + s[i:]


# テスト
print(insertUnderscoreAt("stevejobs", 8))            # stevejob_s
print(insertUnderscoreAt("stevejobs", 9))            # stevejobs
print(insertUnderscoreAt("stevejobs", 5))            # steve_jobs
print(insertUnderscoreAt("stevejobs", 0))            # _stevejobs
print(insertUnderscoreAt("stevejobs", 10))           # stevejobs
print(insertUnderscoreAt("donaldtrump", 6))          # donald_trump
print(insertUnderscoreAt("Baseball is very fun.", 5)) # Baseb_all is very fun.
