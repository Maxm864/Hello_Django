# # 1 С клавиатуры вводится 7-значное число. Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр, если нечетных больше, то найти произведение 1 3 и 6 цифры.
# print('1 адание')
# chislo = int(input())
# a =  [chislo // 1000000, (chislo // 100000) % 10, (chislo // 10000) % 10, (chislo // 1000) % 10, (chislo // 100) % 10, (chislo // 10) % 10,  chislo % 10]
# chet = 0
# neсhet = 0
# for i in a:
#     if i % 2 ==0:
#         chet += 1
#     else:
#         neсhet+=1
# if chet > neсhet:
#     print(sum(a))
# else:
#     print(a[0] * a[2] * a[5])

# 3. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.
print('3 задание')
text = input()
# a = input()
# countU = 0
# countL = 0
# for i in a:
#     if a[i - 1].isupper()and a[i].isupper() :
#         countU += 1
#     elif a[i - 1].islower() and a[i].islower() :
#         countL += 1
# print(f'Upper: {countU} \nLower: {countL}')

# print('верхнего: ',c_up,'\nнижнего: ',c_low)
pair_lower = 0
pair_upper = 0
for i in range(len(text)- 1):
    if text[i + 1].islower() and text[i].islower():
        pair_lower += 1
    if text[i + 1].isupper() and text[i].isupper():
        pair_upper += 1
print(pair_upper,' : пара верхнего регистра')
print(pair_lower,' : пара нижнего регистра')
# # 4 Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются # в списке.
# a = [1,45,3,5,7,7,4,2,12,5,45]
# print('4 задание')
# for i in a:
#     if a.count(i) == 1:
#         print('элементы встр 1 раз', i)
# # 5 Даны два кортежа: Необходимо определить:
# # 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
# print('5 адание')
#
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
#
# if sum(C_1) > sum(C_2):
#     print("\nСумма больше в кортеже C_1 больше ")
# else:
#     print("\nСумма больше в кортеже C_2 больше")
#
# # 2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей
# print(C_1.index(min(C_1)),C_1.index(max(C_1)))
# print(C_2.index(min(C_2)),C_2.index(max(C_2)))
