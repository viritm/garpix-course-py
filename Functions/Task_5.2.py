def average(*elts):
    res = 0
    count = 0
    for el in elts:
        res += el
        count += 1
    return res / count


print(average(1, 2, 3, 4))
