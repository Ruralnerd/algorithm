x, y, w, h = map(int, input().split())

arr = []
arr.extend([x, y, w-x, h-y])
print(min(arr))