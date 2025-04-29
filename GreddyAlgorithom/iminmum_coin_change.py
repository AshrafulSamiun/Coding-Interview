#Greedy algorithm to find the minimum number of coins needed to make a given amount.
def coinChange( coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0

        coins.sort(reverse=True)
        coin_number=0
        for coin in coins:
            if amount==0:
                return coin_number
            else:
                if amount>=coin:
                    coin_number+=amount//coin
                    amount=amount%coin
        if amount>0:
            return -1
        else: return coin_number
        

n=int(input().strip())
coin=list(map(int, input().split()))
amount=int(input().strip())
print(coinChange(coin,amount))


# dynamic programming approach (commented out)
    # dp = [float('inf')] * (amount + 1)
    # dp[0] = 0  # 0 coins to make amount 0

    # for i in range(1, amount + 1):
    #     for coin in coins:
    #         if i >= coin:
    #             dp[i] = min(dp[i], dp[i - coin] + 1)

    # return dp[amount] if dp[amount] != float('inf') else -1