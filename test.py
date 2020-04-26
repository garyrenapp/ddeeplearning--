


def coinChange(coins: List[int], amount: int):
    def dp(n):
        if(n == 0):
            return 0
        if(n < 0):
            return -1 

        res = float('inf')
        for coin in coins:
            sub_p = dp(n - coin)
            if(sub_p == -1 ):
                continue
            res = min(res,sub_p + 1)

        return res if res !=float('inf') else -1 
    
    return dp(amount)
