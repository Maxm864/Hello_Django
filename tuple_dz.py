import random
a = [random.randint(0,10) for i in  range(10)]
a = tuple(a)
print(a,'\n',sum(a))

l = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и','и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')



print("кол-во 'т':", l.count('т'),"\nкол-во 'а':", l.count('а'),"\nкол-во 'и':", l.count('и'))



