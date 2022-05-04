N = int(input())
arr = []
for _ in range(N):
    point = list(map(int, input().split()))
    arr.append(point)

arr.sort()

for x, y in arr:
    print(x, y)

# 파이썬의 sort는 list, tuple도 정렬이 가능하다고 한다.
# 1번 항목을 비교해서 같으면 2번 항목을 비교..하는 식으로