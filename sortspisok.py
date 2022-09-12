a = [9,9,4,6,7,4,5,7,3,2,5,3,6,45,7,8,11]
a.sort()
b = []
for i in a:
    if a.count(i) < 2:
        a.append(i)
        print(i)


