X = input()
N = input()
k = 0
while k == N:
    a, b = map(int, input().split())
    price = a * b
    X = X - price
    k += 1
    if k == N:
        if X == 0:
            print("Yes")
        else:
            print("No")
    else:
        pass
