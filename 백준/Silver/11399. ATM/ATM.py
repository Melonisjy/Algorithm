n = int(input())
p = list(map(int,input().split()))
result = 0

p.sort()
for i in range(1, n+1):
    result += sum(p[0:i])

print(result)