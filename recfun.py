import random
def sum(n):

    if len(n) ==0:
       return 0
    l = n.pop()

    return l + sum(n)
n = random.sample(range(1, 100), 10)
print(n)
print(sum(n))

