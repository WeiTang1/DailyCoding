input = [[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]


def inbound(board,row,col):
    return row>=0 and row < len(board) and col >= 0 and col<len(board[0])

def walk(board, row, col, dir):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    if not inbound(board,row,col) or board[row][col] == "#":
        return
    print board[row][col]
    direc = directions[dir]
    while inbound(board,row+direc[0],col+direc[1]) and board[row+direc[0]][col+direc[1]] != "#":
        row,col = row+direc[0], col + direc[1]
        print board[row][col]
        board[row][col] = "#"
    dir = (dir+1)%4
    walk(board,row+directions[dir][0],col+directions[dir][1],dir)



def solution(input):
    walk(input,0,0,0)



solution(input)