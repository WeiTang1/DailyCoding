import random

def toss_biased():
    return 1 if random.randint(0,10) <= 6 else 0
#
# arr = [0]*2
# for _ in xrange(10000000):
#     arr[toss_biased()] +=1
# print arr

def toss_unbiased():

    (a,b) = (toss_biased(),toss_biased())
    while a^b != True:
        (a, b) = (toss_biased(), toss_biased())
    if (a, b) == (0,1):
        return 1
    else:
        return 0


arr = [0]*2
for _ in xrange(10000000):
    arr[toss_unbiased()] +=1
print arr
