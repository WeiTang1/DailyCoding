import random
def rand7():
    return random.randint(1,7)


def rand5():
    r = (rand7()-1)*7 + rand7()
    while r > 45:
        r = rand7() * 7 + rand7()

    return r%5+1

ans = [0] * 6

for i in range(10000000):
    ans[rand5()] += 1
print ans

