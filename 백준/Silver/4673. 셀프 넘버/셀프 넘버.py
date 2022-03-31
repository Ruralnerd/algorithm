def d(n):
    cnt = 0
    for i in range(len(str(n))):
        cnt += int(str(n)[i])

    return n+cnt

arr1 = list(range(1, 10001))
arr2 = []
for i in range(10000):
    arr2.append(d(i))

arr3 = list(set(arr1)-set(arr2))
arr3.sort()

for j in range(len(arr3)):
    print(arr3[j])

# set은 순서가 없다 sort로 정렬