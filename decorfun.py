

def counter(func):
    def wrap(*args, **kwargs):
        wrap.qwer += 1
        return func(*args, **kwargs)

    wrap.qwer = 0
    return wrap


@counter
def f():
    print("Hi girls")


f()
f()
f()
f()
f()
print('Число вызовов функции:', f.qwer)





