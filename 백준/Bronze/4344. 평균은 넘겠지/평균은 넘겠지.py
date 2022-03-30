C = int(input())


for _ in range(C):
    cnt = 0
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]+1):
        # print(i)
        if arr[i] > sum(arr[1:])/arr[0]:
            # print(arr[i])
            cnt += 1
    print(f"{cnt/arr[0]*100:.3f}%")
    
# round와 f-string 소수점