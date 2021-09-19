a = [1, 2, 3, 4]

for index, num in enumerate(a):
    if num == 2 or num == 3:
        del(a[index])

print(a)
