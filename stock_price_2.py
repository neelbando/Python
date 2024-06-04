from functools import reduce
def stock_buy_sell_2(lst):
    cur_profit = 0
    max_profit = 0
    max_profit_lst = []
    min_buy_price = lst[0]
    
    for i in range(1,len(lst)):

        cur_profit = lst[i] - min_buy_price
        
        if cur_profit < max_profit:
            cur_profit = 0
            if max_profit !=0:
                max_profit_lst.append(max_profit)
            max_profit = 0
            min_buy_price = lst[i]
        else:
            max_profit = cur_profit

            
            
    max_profit_lst.append(max_profit)
    return max_profit_lst, reduce(lambda x,y: x+y,max_profit_lst)

lst1 = [5,2,7,3,6,1,2,4]    #output: [5, 3, 3], 11
print(stock_buy_sell_2(lst1))

# time complexity = O(n)
# can buy or sell stocks multiple time
            