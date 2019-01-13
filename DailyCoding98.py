input = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

def solution(input,word):

    def dfs(row,col,input,word):
        if row<0 or col<0 or row >= len(input) or col >= len(input[0]):
            return False
        if not word:
            return True
        if input[row][col] != word[0]:
            return False
        temp = input[row][col]
        input[row][col] = "#"
        ans = dfs(row+1,col,input,word[1:]) or dfs(row-1,col,input,word[1:]) or dfs(row,col+1,input,word[1:]) or dfs(row,col-1,input,word[1:])
        input[row][col] = temp
        return ans
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == word[0]:
                if dfs(i,j,input,word):
                    return True
    return False

for word in ["ABCCED", "ABCD"]:
    print solution(input,word)