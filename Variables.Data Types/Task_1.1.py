print("Введите ваше ФИО:\n")

full_name = input()

print("Введите адрес доставки:\n")

address = input()

print(
    f"Здравствуйте, {full_name.title().strip()}. Ваш заказ отправлен по адресу {address.title().strip()} ")
