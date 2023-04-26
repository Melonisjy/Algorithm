A, B = map(int,input().split())
a = min(A, B)
b = max(A, B)

n = b-a-1
if a == b or a+1 == b:
    n = 0
print(n)

for i in range(a + 1, b):
    print(i, end=" ")

