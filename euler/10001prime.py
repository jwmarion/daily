# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

numList=[2]
index = 3
t = 0;

while (len(numList)<=10000):
    for x in range(2, int(index ** 0.5)+1):
        if index % x == 0:
            t += 1
    if t == 0:
        numList.append(index)
    index += 1
    t = 0
    print len(numList)

print numList[len(numList)-1]
