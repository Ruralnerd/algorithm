M = int(input())
N = int(input())

arr = []
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if not i % j:
            cnt += 1
    if cnt == 2:
        arr.append(j)
if len(arr) == 0:
    print(-1)

else:
    print(sum(arr))
    print(min(arr))