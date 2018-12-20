import collections

N = 6
X = 12


def solution(N, X):
    arr = [(i+1)*(j+1) for j in range(N) for i in range(N)]
    hm = collections.Counter(arr)
    return hm[X]


def solution2(N, X):
    ans = 0
    for i in range(N):
        for j in range(N):
            if (i+1) * (j+1) == X:
                ans += 1
    return ans


print solution2(N, N)


