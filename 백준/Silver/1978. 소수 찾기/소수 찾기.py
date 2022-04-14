N = int(input())
arr = list(map(int, input().split()))

for i in arr:
    cnt = 0
    for j in range(1, i+1):
        if not i % j:
            cnt += 1
    if cnt != 2:
        N -= 1
        
print(N)

