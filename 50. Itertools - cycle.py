from itertools import cycle

a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 15:
        break
