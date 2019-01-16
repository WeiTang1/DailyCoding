input = [1,2,3,4,5]

def solution(input,target):
    s = sum(input)
    l,r = 0,len(input)-1
    while l < r:
        if s == target:
            return input[l:r+1]
        if s-input[r] >= target:
            s = s-input[r]
            r-=1
        else:
            s-=input[l]
            l+=1


print solution(input,8)
