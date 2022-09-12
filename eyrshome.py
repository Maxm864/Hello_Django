year = int(input('Введите год: '))

if year % 400 == 0:
    print("високосный")
elif year % 100 == 0:
    print("не високосный")
elif year % 4 == 0:
    print("високосный")
else:
    print("не високосный")