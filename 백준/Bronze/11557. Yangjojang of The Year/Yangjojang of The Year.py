T = int(input())
for i in range(T):
    max = 0
    res = ""
    for j in range(int(input())):
        name, num = map(str,input().split())
        if int(num) > max:
            max = int(num)
            res = name
    print(res)


