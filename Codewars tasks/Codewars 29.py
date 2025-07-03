def max_profit(prices):
    
    profit = prices[1] - prices[0]
    min_price = prices[0]
    number_of_prices = len(prices)

    for j in range(1,number_of_prices):

        if profit < prices[j] - min_price:
            profit = prices[j] - min_price

        if prices[j] < min_price:
            min_price = prices[j]

    return profit


print(max_profit([10, 7, 5, 8, 11, 9]))