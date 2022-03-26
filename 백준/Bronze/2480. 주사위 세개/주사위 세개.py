number = sorted(list(map(int, input().split())))

if number[0] == number[1] == number[2]:
    print(10000 + (number[0] * 1000))

elif number[0] == number[1]:
    print(1000 + number[0] * 100)

elif number[1] == number[2]:
    print(1000 + number[1] * 100)

else:
    print(max(number) * 100)