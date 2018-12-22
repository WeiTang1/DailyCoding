input = [(1, 3), (5, 8), (4, 10), (20, 25)]


def solution(input):
    input.sort(cmp = lambda x,y: x[1]-y[1] if x[0]==y[0] else x[0]-y[0])
    ans = []
    for interval in input:
        print interval
        if len(ans) == 0:
            ans.append(interval)
        if interval[0] <= ans[-1][1]:
            prev = ans.pop()
            ans.append((min(prev[0],interval[0]),max(prev[1],interval[1])))
        else:
            ans.append(interval)
    return ans


print solution(input)