# garden = {'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', }
# meadow = {'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', }
# print(garden.intersection(meadow))

a = [1,2,3,4,5,6,7,8,9,0,5,3,7,8]
b = set(a)
c = []
for i in b:
    if (a.count(i) > 1):
        c.append(i)
print('дубликаты',c)










