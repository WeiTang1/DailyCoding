input = [
    "cba",
    "daf",
    "ghi"]

input2 = ["abcdef"]
input3 = [
    "zyx",
    "wvu",
    "tsr"
          ]
def lexiOrder(li):
    for i in range(1,len(li)):
        if li[i]<li[i-i]:
            return False
    return True
def solution(input):
    ans = 0
    for col in range(len(input[0])):
        r = [input[row][col] for row in range(len(input))]
        if not lexiOrder(r):
            ans+=1
    return ans


print solution(input3)
