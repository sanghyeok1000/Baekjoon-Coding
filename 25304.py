X = int(input())  # 총금액
N = int(input())  # 물건 갯수
k = 0  # 뺀 횟수
while k != N:
    a, b = map(int, input().split())
    price = a * b
    X = X - price
    k += 1
if X == 0:
    print("Yes")
else:
    print("No")
