
list = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]
list1 = []

# res = [x for x in list if x != ""]

for el in list:
    if el == "":
        continue
    else:
        list1.append(el)

print(list1)
