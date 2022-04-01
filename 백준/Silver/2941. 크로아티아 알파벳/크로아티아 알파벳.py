sen = input()

lst = ['c=', 'c-', 'dz=', "d-", "lj", "nj", "s=", "z="]

for i in range(len(lst)):
    sen = sen.replace(lst[i], "1", 100)

print(len(sen))