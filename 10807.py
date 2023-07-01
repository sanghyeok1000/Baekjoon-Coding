N = int(input())
count = 0
list = list(map(int, input().split()))
b = int(input())
for i in list:
    if b == i:
        count += 1
print(count)
