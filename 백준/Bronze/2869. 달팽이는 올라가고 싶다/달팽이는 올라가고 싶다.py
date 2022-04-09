A, B, V = map(int, input().split())
# A = 달팽이가 낮에 올라가는 거리
# B = 달팽이가 밤에 내려오는 거리
# V = 막대의 길이

# 나머지가 0이 아니라면 다음날 아침에 도착하는 것
if (V-B) % (A-B):
    print((V-B)//(A-B)+1)
else:
    print((V-B)//(A-B))