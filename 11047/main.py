n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
res = 0

coin = coins.pop()
while k > 0:
    print(coin, k, coins)
    if k >= coin:
        res += k // coin
        k %= coin
    else:
        coin = coins.pop()

print(res)