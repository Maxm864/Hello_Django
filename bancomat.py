a  = int(input('введите кол-во денег'))
run = True
c = 0
print('баланс:',a)
while run:
    b = int(input('введите расход'))
    if b < a :
        a= a-b
        print('баланс:', a)
        c += 1
    elif b > a :
        print('денег не хватило \n баланс: ',a, '\n Количество операций:',c)
    elif b == a:
        a = a - b
        run = False
        c += 1
else:
    print('Количество операций', c,'баланс', a )


