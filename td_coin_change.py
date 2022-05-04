import math
def min(x, y):
    if x < y:
        return x
    else:
        return y


def td_coin_change(coins, v):

    memo = [None] * (v+1)

    if v == 0 :
        return 0
    if memo[v] == None:
        min_coins = math.inf
    for i in range(len(coins)):
        if coins[i] <= v:
            min_coins = min(min_coins, 1+ td_coin_change(coins, v-coins[i]))
    memo[v] = min_coins
    return memo[v]

print(td_coin_change([5,10,20,50], 50))