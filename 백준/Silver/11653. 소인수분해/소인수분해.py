N = int(input())
if N == 1:
    pass

else:
    arr = []
    while N != 1:
        for i in range(2, N+1):
            if not N % i:
                arr.append(i)
                N = N//i
                break

    for i in arr:
        print(i)