for i in range(int(input())):
    option = 0
    s = int(input())
    for j in range(int(input())):

        q, p = map(int,input().split())
        option += q*p
    print(s+option)

