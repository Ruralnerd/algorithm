n = int(input())


def fibo(n):
    temp = [0, 1]
    for i in range(2, n + 1):
        temp.append(temp[i - 1] + temp[i - 2])
    return temp[n]


print(fibo(n))

#메모이제이션