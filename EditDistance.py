def editDistDP(str1, str2):
    # Create a table to store results of subproblems
    dp = [[0 for i in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # Fill d[][] in bottom up manner
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

                # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    for d in dp:
        print d
    return dp[len(str1)][len(str2)]

print editDistDP("ab","acd")


