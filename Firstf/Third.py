from types import new_class


list = list(map(int, input("Введите числа без пробела: ")))
new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)