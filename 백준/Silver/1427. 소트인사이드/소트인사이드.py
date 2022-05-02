N = list(map(int, input()))

N.sort(reverse=True)

print(''.join(str(_) for _ in N))