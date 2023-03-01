for i in range(int(input())):
    a = 0   # 총합
    b = 0   # 평균
    d = 0
    T = int(input())
    for j in range(T):
        c, g = map(float,input().split())
        a += c
        d += c * g
    b = d / a
    print(int(a),'%.1f' %b)

