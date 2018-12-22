input = [15, 5, 20, 10, 35, 15, 10]
input2 = [15, 5, 20, 10, 35]
def getsubset(input,index,li,ans):
    ans.append(li)
    for i in range(index,len(input)):
        getsubset(input,i+1,li+[input[i]],ans)


def solution(input):
    subset  = []
    getsubset(input,0,[],subset)
    for s in subset:
        if sum(s) == sum(input)/2:
            return True
    return False


def solution2(input):
    s = sum(input)/2
    dp = [[False for _ in range(s+1)] for _ in range(len(input)+1)]
    dp[0][0] = True
    for i in range(1,len(input)):
        dp[i][0] = True
    for j in range(1,s+1):
        dp[0][j] = False

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
                dp[i][j] = dp[i - 1][j]
                if j >= input[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-input[i-1]]
    return dp[len(input)][s]


print solution2(input)