import re


def countOfOccurence(path, word):
    with open(path, encoding="utf-8") as f:
        return len(re.findall(f"(?<=\W){word}(?=\W)", f.read()))


print(countOfOccurence("../Data/Test.txt", "молчал"))
print(countOfOccurence("../Data/Test.txt", "про"))
