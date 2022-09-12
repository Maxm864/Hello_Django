# Задача№1
# Значениями словаря могут быть и списки. Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений. Выведите первое и последнее значения каждого из ключей.
dict_car = {'BMW':'mark1',
            'sfg':'adsf',
            'dfg0':4646,
            'Tesla': ['mark1', 'mark2', 'mark3']
            }
for key,value in dict_car.items():
    if isinstance(value, str):
        print(key)
# Задача№2
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
dict_c = {'a':1,'b':2,'c':3,'d':4,'e':5}
pr = 1
for k in dict_c:
    pr = pr * dict_c[k]
print(pr)