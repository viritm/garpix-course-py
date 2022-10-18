class MyEroor(Exception):
    def __init__(self, text):
        self.textError = text


def check_name(name):
    numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    for symb in name:
        if symb in numbers:
            raise MyEroor("Имя не может содержать в себе цифры")
    print(name)


check_name("Вася")
check_name("Сан1к")
