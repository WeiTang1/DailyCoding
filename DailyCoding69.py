input = [-10, -10, 5, 2]



def bfs(input, li, index):
    ans = float('-inf')
    if len(li) == 3:
        _ans = 1
        for num in li:
            _ans *=num
        ans = max(ans,_ans)
        return ans

    for i in range(index,len(input)):
        if i > index and input[i-1] == input[i]:
            continue
        ans = max(ans,bfs(input, li+[input[i]], i+1))
    return ans


def solution(input):
    return bfs(input,[],0)


print solution(input)