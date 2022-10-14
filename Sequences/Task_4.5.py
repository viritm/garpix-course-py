
lst1 = ['Санкт-Петербург', 'Москва', 'Казань', 'Волгоград', 'Калининград']
lst2 = ['Самара', 'Калининград', 'Воронеж', 'Санкт-Петербург', 'Иваново']

set1 = set(lst1)
set2 = set(lst2)

intersection = list(set1.intersection(set2))
difference = list(set1.symmetric_difference(set2))

print(intersection)
print(difference)
