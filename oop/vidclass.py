class test1:

    @staticmethod
    def add(a,b):
        return a +b

    @staticmethod
    def sub(a, b):
        return a - b

print(test1.add(15,56))
print(test1.sub(56,15))


class test2:

    min = 0
    max = 100

    @classmethod
    def vel(cls,a):
        return cls.min <= a <= cls.max

print(test2.vel(56))

