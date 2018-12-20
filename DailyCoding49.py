arr =  [34, -50, 42, 14, -5, 86]

def bruteforce(arr):
    maxsum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            s = sum(arr[i:j+1])
            maxsum = s if s>maxsum else maxsum

    return maxsum
print bruteforce(arr)

def dp(arr):
    maxsum,maxsofar = 0,0
    for num in arr:
        maxsofar += num
        if maxsofar<0:
            maxsofar = 0
        else:
            maxsum = maxsofar if maxsofar>maxsum else maxsum

    return maxsum

print dp(arr)