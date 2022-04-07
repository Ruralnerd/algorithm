X = int(input())

line = 0
end_point = 0

while X > end_point:
    line += 1
    end_point += line

idx = end_point - X

if line % 2:
    up = idx + 1
    down = line - idx

else:
    up = line - idx
    down = idx + 1

print(f'{up}/{down}')