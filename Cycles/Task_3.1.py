
count = 0
N = input("Enter count of numbers: ")
for i in range(int(N)):
    el = input("Введите число: ")
    if int(el) % 2 == 0:
        count += 1

print(f"Count of even numbers = {count}")
