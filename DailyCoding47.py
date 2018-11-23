prices = [9, 11, 8, 5, 7, 10]
def buyandsell(prices):
    currentmin = prices[0]
    profit = 0
    for i, price in enumerate(prices):
        if price < currentmin:
            currentmin = price
        elif price>currentmin:
            profit = price - currentmin
    return profit


print buyandsell(prices)