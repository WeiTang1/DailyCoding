def dfs(row,col,n,m):
    if row == n-1 and col == m-1:
        return 1
    count = 0
    if row+1 < n:
        count+=dfs(row + 1, col, n, m)
    if col+1 <m:
        count += dfs(row,col+1,n,m)
    return count


def solution2(n,m):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for row in range(n-1,-1,-1):
        for col in range(m-1,-1,-1):
            if row == n-1 or col == m-1:
                dp[row][col] = 1
                continue
            dp[row][col] = dp[row+1][col] + dp[row][col+1]
    return dp[0][0]



def solution(n,m):

    return dfs(0,0,n,m)

print solution2(5,5)