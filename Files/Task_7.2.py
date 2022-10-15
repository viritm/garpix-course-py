

def read_last(lines, file):
    with open(file, encoding="utf-8") as f:
        myList = f.readlines()
        countOfLines = len(myList)
        temp = [line.replace("\n", "") for line in myList[countOfLines-lines:]]
        temp.reverse()
        res = "\n".join(temp)
        return res


print(read_last(5, "../Data/Verse.txt"))
