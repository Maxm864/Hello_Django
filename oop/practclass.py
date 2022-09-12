class Prract:


    def func1(self, arg):
        if isinstance(arg, str):
            if sum( x in "qwrtypsdfghklzxcvbnm" for x in arg) * sum( x not  in "qwrtypsdfghklzxcvbnm" for x in arg) <= self.func2(arg):
                return ''.join([x for x in arg if x in "qwrtypsdfghklzxcvbnm"])
            else:
                return ''.join([x for x in arg if x not in "qwrtypsdfghklzxcvbnm"])
        elif isinstance(arg, int):
            return sum(int(x) for x in str(arg) if x in "02468") * self.func2(arg)


    def func2(self, arg):
        return len(str(arg))

awe = Prract()
test1 = awe.func1(23456)
test2 = awe.func1('qawsed')

print(test1)
print(test2)

