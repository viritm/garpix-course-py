def findLongestWords(path):
    wordList = []
    biggestLength = 0
    with open(path, encoding="utf-8") as f:
        text = f.read()
        for el in text.split():
            if len(el) > biggestLength:
                wordList.clear()
                wordList.append(el)
                biggestLength = len(el)
            elif len(el) == biggestLength:
                wordList.append(el)
    return wordList


print(findLongestWords("../Data/Test.txt"))
