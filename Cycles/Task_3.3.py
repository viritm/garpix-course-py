lst = [10, 17, 13, 44, 23, 88, 100, 99]

print("Only even:")
for el in lst:
    if el % 2 == 0:
        print(el)

print("Only odd:")
for el in lst:
    if el % 2 != 0:
        print(el)
