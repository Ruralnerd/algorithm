h, m = map(int, input().split())

if h >= 1:
    time = (h*60+m)-45
    newH = time//60
    newM = time%60

elif h == 0:
    if m < 45:
        cnt = 45 - m
        newH = 23
        newM = 60-cnt
    else:
        newH = 0
        newM = m - 45

print(newH, newM)