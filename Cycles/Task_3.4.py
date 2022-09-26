# with if

for el in range(1, 1000001):
    if el % 2 == 0:
        print(el)


# without if

count = 0
while count != 1000000:
    count += 2
    print(count)
