N = int(input())

cnt = 0

for _ in range(N):
    sen = input()

    for i in range(len(sen)):
        if i != len(sen)-1:
            if sen[i] == sen[i+1]:
                pass
            elif sen[i] in sen[i+1:]:
                break
        # len(sen)이 1일 경우 무조건 그룹 단어이므로 + 1
        # 모든 반복문을 pass 했을 경우 그룹 단어이므로 + 1
        else:
            cnt += 1
            
print(cnt)

# 오래걸림