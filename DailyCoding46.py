str = "aabcdcb"
str2 = "bananas"

def longestPalidromeSubsequenceLength(str):
    dp = [[0 for x in range(len(str))] for x in range(len(str))]

    for i in range(len(str)):
        dp[i][i] = 1

    for i in range(len(str)-2,-1,-1):
        for j in range(i+1,len(str)):
            if j == (i+1):
                    dp[i][j] = 2 if str[i] == str[j] else 1
            elif str[i] == str[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    for d in dp:
        print d


def longestPalindrome(s):
    n = len(s)
    dp = [[False for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = True
    max = (0,0)
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if j == (i+1):
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
            if dp[i][j]:
                if (j-i) >(max[1]- max[0]):
                    max = (i,j)
    return s[max[0]:max[1]+1]

# [1, 2, 2, 2, 2, 3, 5]0,1
# [0, 1, 1, 1, 1, 3, 5]1,2
# [0, 0, 1, 1, 1, 3, 5]2,3
# [0, 0, 0, 1, 1, 3, 3]3,4
# [0, 0, 0, 0, 1, 1, 1]4,5
# [0, 0, 0, 0, 0, 1, 1]5,6
# [0, 0, 0, 0, 0, 0, 1]6 n = 7
# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq
# print longestPalidromeSubsequenceLength(str)

print longestPalindrome(str2)
