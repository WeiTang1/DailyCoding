def isPrime(number):
    return all(number % i for i in xrange(2, number))

input = 6

def solution(input):
    ans = []
    for i in range(2,4):
        if isPrime(i):
            ans.append(i)
    l,r = 0,len(ans)-1
    while l <=r:
        if (ans[l] + ans[r]) == input:
            return ans[l],ans[r]
        if ans[l]+ans[r]>input:
            r-=1
        else:
            l+=1



print solution(input)