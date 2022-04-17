# 소수 리스트를 만드는 것부터 다시 생각하자
# 0과 1은 무조건 소수가 아님(False 2개, 나머지는 True로 시작)
prime_list = [False, False] + [True]*10000
# 2부터 1만까지의 배수를 모두 없애기 위함
for i in range(2, 10002):
    # prime_list[i]번째가 True로 되어있다면
    if prime_list[i]:
        # 해당 배수들을 모두 False로 바꾼다(체)
        for j in range(2*i, 10002, i):
            prime_list[j] = False

T = int(input())

for _ in range(T):
    n = int(input())
    a = b = n//2
    while a:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1