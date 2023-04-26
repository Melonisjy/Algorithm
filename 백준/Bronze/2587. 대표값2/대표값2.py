arr = []

for i in range(5):
    num = int(input())
    arr.append(num)

avg = int(sum(arr) / 5)
print(avg) # 대표값 출력

arr.sort()
center = arr[2]
print(center)