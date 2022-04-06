A, B, C = map(int, input().split())

if B >= C:
    print(-1)

else:
    print(A//(C-B)+1)

# 수학적으로 접근하는 사고를 하자