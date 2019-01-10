input = [
            [1, 0 ,0, 0 ,0]
,[0 ,0 ,1 ,1 ,0]
,[0 ,1 ,1 ,0, 0]
,[0 ,0 ,0 ,0 ,0]
,[1, 1 ,0 ,0 ,1]
,[1, 1 ,0 ,0 ,1]
]

def dfs(matrix,row,col):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    stack = [(row,col)]
    while stack:
        _r,_c = stack.pop()
        matrix[_r][_c] = "*"
        for dir in directions:
            nr,nc = map(lambda x,y:x+y, dir,(_r,_c))
            if nr>=0 and nr<len(matrix) and nc>=0 and nc< len(matrix[0]) and matrix[nr][nc] not in [0,"*"]:
                stack.append((nr,nc))

def solution(matrix):
    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                dfs(matrix,i,j)
                ans+=1
    return ans

print solution(input)