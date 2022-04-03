lst = ["0", "0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

alp = input()
ans = 0
for i in range(len(alp)):
    for j in range(len(lst)):

        if alp[i] in lst[j]:
            ans += j

print(ans)