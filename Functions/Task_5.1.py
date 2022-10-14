def perimetr(*sides):
    sum = 0
    for el in sides:
        sum += el
    return sum


print(perimetr(1, 2, 3, 10))
