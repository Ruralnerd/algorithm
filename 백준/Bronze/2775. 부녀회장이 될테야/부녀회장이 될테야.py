T = int(input())

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호수
    # 2층에 3호라고 치자
    # i는 0, 1을 돈다
    # j는 1,2,3을 돈다
    arr = [[0]*14 for _ in range(k+1)]
    for i in range(k+1):
        for j in range(14):
            if i == 0:
                arr[i][j] = j+1
            else:
                arr[i][j] = arr[i-1][j]+arr[i][j-1]


    print(arr[k][n-1])
