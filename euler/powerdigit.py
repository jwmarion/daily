# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

n = str(2 ** 1000)
r = 0
for x in n:
    r += int(x)

print r
