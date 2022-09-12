a = input('Введите число')
c = ''
for i in a:
    if int(i) % 2 != 0:
        continue
    c = c + i
print(c)



