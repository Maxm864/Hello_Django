a = [4,6,'pу','tell',78]

b = [44,'hello',56,'exept',['world',5.7],3,6]
# 1 сложіть два спіска
# a.extend(b)
print(a+b)
# 2 Добавить элемент 6 на 3 позицию.

a.insert(2,6)
print('\n',a)
# 3. Посчитать сколько раз встречается число 6
c = 0
for i in a:
    if i ==6:
        c += 1
print('\nкол-во 6 -',c)
# 4. Посчитать количество элементов списка
d = len(a)
print('\nкол-во элементов',d)
# 5. Вывести 1 элемент вложенного списка

# print(a[9][0])



