passenger = 0
max_passenger = 0
for i in range(10):
    a, b = map(int,input().split())
    passenger += b - a
    max_passenger = max(passenger, max_passenger)
print(max_passenger)