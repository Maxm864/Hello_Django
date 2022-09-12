# def funk_1 (*args,**kwargs):
#
#     print(args[1::2])
#     for  k , v in kwargs.items() :
#         if isinstance(v,str):
#             print(k + ' = ' + v)
#
# funk_1(1,2,3,4,5,6,7,8,a='4545',b=9,c=3,s='fg')
#
def is_prime(x):
    result = (x == 2 or x % 2 != 0)
    if result:
        for i in range(3, int(x**0.5), 2):
            if x % i == 0:
                return False

    return result

print(is_prime(27))