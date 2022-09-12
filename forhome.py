a = int(input('Введите трехначное число'))

sum=0
for i in range (3):
    sum = sum + a%10
    a = a//10
print(sum)
