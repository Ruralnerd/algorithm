prime_list = []

for i in range(1, 123456*2):
    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        prime_list.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break

    for i in prime_list:
        if n < i <= n*2:
            cnt += 1

    print(cnt)

# 미리 소수 리스트를 만들어두는 것이 시간이 덜 걸렸다