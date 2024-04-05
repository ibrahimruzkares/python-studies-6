import itertools

letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]


result = itertools.combinations(letters, 2)             #seçilim
result2 = itertools.permutations(letters, 2)            #sıralama - aynı elemanlar tersten yazılabilir


for item in result:
    print(item)

# for item in result2:
#     print(item)
