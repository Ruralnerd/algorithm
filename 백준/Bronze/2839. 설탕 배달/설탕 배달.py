N = int(input())
# 총 설탕의 무게

temp = N//5
temp2 = N//3
ans = []

if not N%5:
    print(temp)

else:
    for i in range(temp, -1, -1):
        for j in range(temp2+1):
            if (5*i)+(3*j) == N:
                ans.append(i+j)

    if not len(ans):
        print(-1)
    else:
        print(min(ans))

