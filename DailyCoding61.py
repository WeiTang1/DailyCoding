def solution(x,y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return solution(x,y/2) * solution(x,y/2)
    else:
        return x* solution(x,y/2) * solution(x,y/2)

print solution(5,5)