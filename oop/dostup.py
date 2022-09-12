# class test:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     def set(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get(self):
#         return self.__x ,self.__y
#
#
# t = test(1,3)
# t.set(10,20)
# print(t._x, t._y)
# print(t.get())

a = input("что-то")
b = input('что-то')
c = 0
for i in a:
    if i == b :
        c+=1

    if c == 0:
        print('no')
print(c)

