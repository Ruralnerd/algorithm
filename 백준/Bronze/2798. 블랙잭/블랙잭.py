N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            add = arr[i]+arr[j]+arr[k]
            if ans < add <= M:
                ans = add

print(ans)