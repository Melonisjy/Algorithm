list1 = []
for i in range(10):
    list1.append(int(input()))

print(int(sum(list1)/10))
print(max(list1, key=list1.count))
