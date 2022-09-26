password = "psj45L"


while True:
    response = input("Enter a password or 'q' to finish: ")
    if response == 'q':
        break
    elif response == password:
        print("Good job")
    else:
        print("Try again")
