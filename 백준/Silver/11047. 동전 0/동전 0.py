n, k = map(int,input().split())
coins = []
count = 0


for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    count += k // coin
    k %= coin 

print(count)