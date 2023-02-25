maxNum = 0 
maxIndex = 0
for i in range(5):
    a, b, c, d = map(int,input().split())
    res = a+b+c+d
    if maxNum < res:
        maxNum = res
        maxIndex = i+1
print(maxIndex, maxNum)
