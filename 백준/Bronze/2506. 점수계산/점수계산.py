n = int(input())
sum = 0
res = 0

lst = list(map(int,input().split()))
for i in range(n):
    if lst[i] == 1:
        sum += 1
        res += sum
    else:
        sum = 0
         
print(res)

