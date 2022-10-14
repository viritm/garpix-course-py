
def GetFirstSixLines(path):
    res = ""
    with open(path, encoding="utf-8") as f:
        for el in range(6):
            res += f.readline()
        return res


print(GetFirstSixLines("/home/evgeny/python/garpix-course-py/Data/Verse.txt"))
