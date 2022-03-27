A = int(input())
B = int(input())
C = int(input())

mul_lst = list(map(int, str(A*B*C)))

for i in range(10):
    print(mul_lst.count(i))