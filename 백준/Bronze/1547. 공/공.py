ball = [0, 1, 0, 0]
for i in range(int(input())):
    x, y = map(int,input().split())
    ball[x], ball[y] = ball[y], ball[x]
print(ball.index(1))
