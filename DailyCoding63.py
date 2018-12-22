input = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

word = "FOAM"
def solution(input,word):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == word[0]:
                #left to right
                r,c = i,j
                for k in range(len(word)):
                    if c>= len(input[0]) or word[k]!=input[r][c]:
                        break
                    c+=1
                else:
                    return True
                r,c = i,j
                #up to down:
                for k in range(len(word)):
                    if r >= len(input) or word[k] != input[r][c]:
                        break
                    r+=1
                else:
                    return True

    return False
print solution(input,"FOAM")