N = int(input())

def d(n):
    count = 0
    n = list(map(int, str(n)))
    if len(n) == 1:
        count = 1
    else:
        arr = []
        for i in range(len(n)-1):
            arr.append(int(n[i+1])-int(n[i]))
        if len(set(arr)) == 1:
            count = 1

    return count


ans = 0
for i in range(1, N+1):
    ans += d(i)

print(ans)