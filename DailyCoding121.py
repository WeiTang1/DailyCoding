
def subsequence(s):
    if not s:
        return [""]
    if len(s)== 1:
        return [s]
    ans = [s[0]]
    i = 1
    while i < len(s) and s[i] == s[i-1]:
        i+=1
    for subs in subsequence(s[i:]):
        ans.append(subs)
        ans.append(s[0]+subs)
    return ans

def subsequencewithduplicate(s):

    def backtracking(ans,path,s,idx):
        ans.append(path)

        for i in range(idx,len(s)):
            if i > idx and s[i]== s[i-1]:
                continue
            backtracking(ans,path+s[i],s,i+1)

    ans = []
    backtracking(ans,"",s,0)
    return ans

def solution(input,k):

    subsequences = subsequencewithduplicate(input)
    subsequences = filter(lambda x: len(x) >=len(input)-k, subsequences)
    subsequences = filter(lambda x: x == x[::-1],subsequences)
    return len(subsequences)  > 0

print solution("waterretaw",2)