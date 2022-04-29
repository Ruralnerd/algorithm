N = int(input())

cnt = 666
arr = []
while True:
    if '666' in str(cnt):
        arr.append(cnt)
    cnt += 1
    if len(arr) > N:
        break

print(arr[N-1])