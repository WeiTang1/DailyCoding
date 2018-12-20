biships = [(0, 0),
(1, 2),
(2, 2),
(4, 0),
           (3,1)
           ]

m = 5
#
# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 b 0 0 0]
# [b 0 0 0 0]


def solution(biships, m ):
    ans = 0
    for i in range(m):
        row,col = 0,i
        biship = 0
        while row>=0 and row<m and col>=0 and col<m:
            if (row,col) in biships:
                biship+=1
            row+=1
            col-=1
        ans += ((biship-1)*(biship)/2) if biship>1 else 0
    for i in range(1,m):
        row,col = i,m-1
        biship = 0
        while row>=0 and row<m and col>=0 and col<m:
            if (row,col) in biships:
                biship+=1
            row+=1
            col-=1
        ans += ((biship-1)*(biship)/2) if biship>1 else 0

    for i in range(m):
        row,col = 0,i
        biship = 0
        while row>=0 and row<m and col>=0 and col<m:
            if (row,col) in biships:
                biship+=1
            row+=1
            col+=1
        ans += ((biship-1)*(biship)/2) if biship>1 else 0
    for i in range(1,m):
        row,col = i,0
        biship = 0
        while row>=0 and row<m and col>=0 and col<m:
            if (row,col) in biships:
                biship+=1
            row+=1
            col+=1
        ans += ((biship-1)*(biship)/2) if biship>1 else 0
    return ans

print solution(biships,m)