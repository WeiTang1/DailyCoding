input = [1,2,3]


def dfs(li, input, ans):
    if 0==len(input):
        ans.append(li)
        return
    for i in range( len(input)):
        if i > 0 and input[i] == input[i - 1]:
            continue
        dfs(li + [input[i]], input[:i]+input[i+1:], ans)


def solution(input):


    ans = []
    input.sort()
    dfs([],input,ans)
    return ans

print solution(input)