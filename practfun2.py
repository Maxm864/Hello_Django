def over():
    return exit()

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a,b):
    if b !=0:
        return a / b
    else:
        return  ' делить на ноль нельзя'

while True:
    print("Введите операцию + - * /.\nЕсли хотите выйти нажмите 0")
    z = input("")
    if z == '0':
        s = over()
        print(s)
    elif z == '+':
        print("Введите число a")
        a = float(input())
        print("Введите число b")
        b = float(input())
        print("============================")
        s = add(a,b)
        print('%.2f' %  s)
    elif z == '-':
        print("Введите число a")
        a = float(input())
        print("Введите число b")
        b = float(input())
        print("============================")
        s = sub(a,b)
        print('%.2f' %  s)
    elif z == '*':
        print("Введите число a")
        a = float(input())
        print("Введите число b")
        b = float(input())
        print("============================")
        s = mul(a, b)
        print('%.2f' %  s)
    elif z == '/':
        print("Введите число a")
        a = float(input())
        print("Введите число b")
        b = float(input())
        print("============================")
        s = div(a, b)
        print(s)



def func(a):

    if isinstance(a, tuple):
        p = 0
        for i in a:
            for s in str(i):
                if isinstance(i,str):
                    p +=1
        print(p)

    elif isinstance(a,list):
        al = 0
        num = 0
        for i in a:
            for s in str(i):
                if isinstance(i,str) and not s.isdigit():
                    al += 1
                else :
                    num += 1
        print('букв',al,'цифр',num)

    elif isinstance(a,int):
        digits = "13579"
        nechet = 0
        for i in str(a):
            if i in digits:
                nechet += 1
        print('кол-во нечетных цифр', nechet)

    elif isinstance(a, str):
        print(len(a), 'букв')
    else:
        print("неизвестрный тип")

func(('123','3p575',4678))
func(['1k56l',6798,'8uo9lp'])
func(137576)
func('qwertyu')
func({1:56})





