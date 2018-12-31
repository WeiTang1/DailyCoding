input = "()())()"
input2 = ")("
def isValid(str):
    if not str or str == "":
        return True
    stack = []
    for char in str:
        if char == '(':
            stack.append("(")
        elif char == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            else:
                stack.pop()

    return len(stack) == 0




testcases = ["","()",")(","))(","(())","()()",'(()))',')())()())((()']

def helper(str,idx,ans):
    if isValid(str):
        ans = min(idx,ans)
    else:
        for i in range(len(str)):
            tmp = str[:i]+str[i+1:]
            ans = min(ans, helper(tmp,idx+1,ans))
    return ans

def solution(str):
    return helper(str,0,float("+inf"))

def solution2(str):
    if not str:
        return 0
    stack = []
    ans = 0
    for char in str:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if len(stack)==0 or stack[-1] != "(":
                ans+=1
            else:
                stack.pop()
    return ans + len(stack)

print solution2("))(()())")