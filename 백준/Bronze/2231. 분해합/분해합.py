N = int(input())

for i in range(1,N+1):
    temp_sum = sum(map(int, str(i)))
    create_num = i + temp_sum
    if create_num == N:
        print(i)
        break

    if i == N:
        print(0)