def sum(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise Exception("Ожидаемый тип данных - число")
    else:
        return x+y


print(sum(3, 2.0))
