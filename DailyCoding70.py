n =1

def isPerfect(number):
    return sum([int(i) for i in list(str(number))]) == 10

def solution(n):
    number = 0
    while True:
        if isPerfect(number):
            n-=1
            if n==0:
                return number
        number+=1


print solution(2)