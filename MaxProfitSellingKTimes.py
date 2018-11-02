# Input:
# Price = [10, 22, 5, 75, 65, 80]
#     K = 2
# Output:  87
# Trader earns 87 as sum of 12 and 75
# Buy at price 10, sell at 22, buy at
# 5 and sell at 80

price = [10, 22, 5, 75, 65, 80]

k = 2

def maxtradeValue(price, k):
    matrix = [[0 for i in range(k+1)] for j in range(len(price))]
    #matrix[i][j]
    for day in range(1,len(price)):
        for transaction in range(1,k+1):
            max_so_far = 0;

            for i in range(day):
                max_so_far = max(max_so_far, price[day]-price[i]+matrix[i][transaction-1])
            matrix[day][transaction] = max(matrix[day-1][transaction],max_so_far)
    print matrix
maxtradeValue(price,k)
