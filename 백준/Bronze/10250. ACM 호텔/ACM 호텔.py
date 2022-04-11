T = int(input())

for _ in range(T):
    arr = []
    H, W, N = map(int, input().split())

    for j in range(1, W+1):
        for i in range(1, H+1):
            if len(str(j))<=1:
                arr.append(str(i)+'0'+str(j))
            else:
                arr.append(str(i)+str(j))

    print(arr[N-1])