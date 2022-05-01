N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(*sorted(arr), sep='\n')