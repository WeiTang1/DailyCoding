def solution(x,y,b):
    if (b>>31) + (-b << 31) == 0:
        return x
    else:
        return y

print solution("0","1",0)