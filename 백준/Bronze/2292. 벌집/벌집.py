N = int(input())

temp = 1
ans = 1

while N > temp:
    temp += ans*6
    ans += 1

print(ans)