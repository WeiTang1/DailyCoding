import random
import operator


t = 0

f = 0


def rand5():
    return random.randint(1,5)

def rand6():

    r = rand5()
    if random.random() < operator.truediv(1,6):
        r = 6
    return r

def rand7():
    r = rand5()
    if random.random() < operator.truediv(1,6):
        r = 6
    if random.random() < operator.truediv(1,7):
        r = 7
    return r
arr = [0]*8
for i in range(10000000):
    arr[rand7()]+=1

print arr
