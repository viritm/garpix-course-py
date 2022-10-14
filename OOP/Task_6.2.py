class ListWorker:
    def __init__(self, *args) -> None:
        self.myNumbers = []
        self.myStrings = []
        self.others = []
        for el in args:
            if (type(el) is str):
                self.myStrings.append(el)
            elif ((type(el) is int) or (type(el) is float)):
                self.myNumbers.append(el)
            else:
                self.others.append(el)

    def getNumbers(self):
        return self.myNumbers

    def getString(self):
        return self.myStrings

    def getOthers(self):
        return self.others


test = ListWorker(1, 2, 3, 4, "abc", "Volgograd",
                  "Emil", {1, 3, 4, 5}, [2, 3, "abc"])
print(test.getNumbers())
print(test.getOthers())
print(test.getString())
