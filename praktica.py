# №1 Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы. Посчитать
# цену выбранных товаров и сколько товаров осталось в изначальном списке
# 6. До свидания
# a = {'napolion': ['muka', 'sol', 'moloko', 'ucsus', 500, 2400],
#      'maphin': ['muka', 'sol', 'moloko', 'ucsus', 850, 1900],
#      'pirozenoe': ['muka', 'sol', 'moloko', 'ucsus', 300, 1300],
#      }
# c = 0
# run = True
# while run:
#     print("Введите 1 если хотите посмотреть описание")
#     print("Введите 2 если хотите посмотреть цену")
#     print("Введите 3 если хотите посмотреть количество")
#     print("Введите 4 если хотите посмотреть Всю информацию")
#     print("Введите 5 чтобы приступить к покупке")
#     print("Введите 6 чтобы закончить")
#     zapros = input(" ")
#     if zapros == '1':
#         for k, v in a.items():
#             print(f'Название: {k}, описание:{v[0:4]}\n')
#     elif zapros == '2':
#         for k, v in a.items():
#             print(f'Название: {k}, цена за 100гр:{v[4]}\n')
#     elif zapros == '3':
#         for k, v in a.items():
#             print(f'Название: {k}, коливество грамм:{v[5]}\n')
#     elif zapros == '4':
#         for k, v in a.items():
#             print(f'Название: {k}, состав:{" ".join(v[0:4])} - цена за 100гр:{v[4]} - коливество грамм:{v[5]}\n')
#     elif zapros == '5':
#         naz = input("Введіте товар, который хотите купить или введите n для выхода")
#         if naz =='n' or naz not in a:
#             break
#         qty = int(input("Сколько вы хотите купить"))
#         if qty>a[naz][5]:
#             print("У нас нет, выбирите другое количество или товар")
#             continue
#         c += qty * a[naz][4]
#         a[naz][5]-= qty
#         print(f"Сумма выбраных товаров: {c}")
#         for k, v in a.items():
#             print(f'Название: {k}, состав:{" ".join(v[0:4])} - цена за 100гр:{v[4]} - коливество грамм:{v[5]}\n')
#     elif zapros =='6':
#         print("Досвидания")
#         run = False
#     №2 Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
# a = {1,2,3,4,5,6,7,8,9}
# b = {1,12,13,4,5,6,17,8,19}
# print(len(a.intersection(b)))
# №3 В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.
f = open("pr.txt",'r')
c = f.read()
f.close()
c = c.split('\n')
arc = 0
for line in c:
    line = line.split(' ')
    if int(line[2]) < 3:
        print('учащиеся чья оценка ниже 3:', " ".join(line))
    arc += int(line[2])
arc/= len(c)
print("средняя оценка :",'%.2f' % arc )
