N = int(input())
people_lst = []

for _ in range(N):
    w, h = map(int, input().split())
    people_lst.append((w,h))

ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if people_lst[i][0] < people_lst[j][0] and people_lst[i][1] < people_lst[j][1]:
            cnt += 1
    ans.append(cnt)
    
print(*ans)