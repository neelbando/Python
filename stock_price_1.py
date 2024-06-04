def stock_buy_sell(lst):
    cur_profit = 0
    max_profit = 0
    min_buy_price = lst[0]
    
    for i in range(1,len(lst)):
        if lst[i] > min_buy_price:
            cur_profit = lst[i] - min_buy_price
            max_profit = max(max_profit,cur_profit)
        else:
            cur_profit = 0
            min_buy_price = lst[i]
    return max_profit

lst1 = [3,5,1,7,4,9,3]    #output: 8  
print(stock_buy_sell(lst1))

# time complexity = O(n)
# can only buy and sell once
            