input = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


def solution(input):
    dp = [1 for i in range(len(input))]

    for i in range(len(input)):
        candidate = 1
        for j in range(i):
            if input[i]>input[j]:
                candidate = max(candidate,dp[j]+1)
        dp[i] = candidate
    return max(dp)

print solution(input)