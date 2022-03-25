h, m = map(int, input().split())
t = int(input())

temp = m+t

if temp >= 60:
    if h + (temp//60) >= 24:
        print((h+temp//60) % 24, temp % 60)
    else:
        print(h+(temp//60), temp % 60)


else:
    print(h, temp)