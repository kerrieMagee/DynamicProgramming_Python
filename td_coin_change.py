import math
def min(x, y):
    if x < y:
        return x
    else:
        return y


def td_coin_change(coins, v):
    """Top down coin change 
       Input: coins - list of length n denominations, v - value where v is the size of v 
       Output: Least no of coins to make up a given value
       Time Complexity: Since sub-problems our solved in v+1 sub problems and each tries all n coins O(n V)
       Space Complexity: O(V) 
       """

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
