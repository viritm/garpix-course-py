
my_list = []

while True:
    str = input("Введите строку или нажмите 'q' для остановки: ")
    if str == 'q':
        break
    else:
        my_list.append(str)

print(my_list)
